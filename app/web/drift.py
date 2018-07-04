# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 16:05
  鱼漂相关视图函数
"""
from flask import flash, redirect, url_for, render_template, request
from flask_login import login_required, current_user
from sqlalchemy import desc, or_

from forms.book import DriftForm
from libs.email import send_mail
from libs.enums import PendingStatus
from models.base import db
from models.drift import Drift
from models.gift import Gift
from models.user import User
from models.wish import Wish
from view_models.book import BookViewModel
from view_models.drift import DriftCollection
from . import web

__author__ = 'Cphayim'


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    """
    发起鱼漂交易
    :param gid: 礼物 id
    :return:
    """
    # 查找礼物
    current_gift = Gift.query.get_or_404(gid)

    # 自己不能向自己请求书籍
    if current_gift.is_yourself_gift(current_user.id):
        flash('这本书是你自己的^_^，不能向自己所要书籍噢')
        return redirect(url_for('web.book_detail', isbn=current_gift.isbn))

    # 能否发起鱼漂
    can = current_user.can_send_drift()
    if not can:
        return render_template('not_enough_beans.html', beans=current_user.beans)

    form = DriftForm(request.form)
    if request.method == 'POST' and form.validate():
        save_to_drift(form, current_gift)
        # 向赠书者发送一份邮件提醒有人向他索取
        send_mail(current_gift.user.email, '有人想要一本书', 'email/get_gift.html',
                  wisher=current_user,
                  gift=current_gift)
        return redirect(url_for('web.pending'))

    # 赠送者简要信息
    gifter = current_gift.user.summary
    return render_template('drift.html', gifter=gifter, user_beans=current_user.beans, form=form)


@web.route('/pending')
@login_required
def pending():
    """
    鱼漂列表视图函数
    :return:
    """
    # 查询当前用户作为索要者或赠送者的所有鱼漂记录
    drifts = Drift.query.filter(
        or_(Drift.requester_id == current_user.id, Drift.gifter_id == current_user.id)
    ).order_by(
        desc(Drift.create_time)
    ).all()
    drift_collection = DriftCollection(drifts, current_user.id)
    return render_template('pending.html', drifts=drift_collection.data)


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    with db.auto_commit():
        drift = Drift.query.filter_by(gifter_id=current_user.id, id=did).first_or_404()
        # 将状态修改为 Reject
        drift.pending = PendingStatus.Reject.value
        # 返还鱼豆给鱼漂发起者
        requester = User.query.get_or_404(drift.requester_id)
        requester.beans += 1

    return redirect(url_for('web.pending'))


@web.route('/drift/<int:did>/redraw')
@login_required
def redraw_drift(did):
    """
    撤销鱼漂视图函数
    :param did: 鱼漂 id
    :return:
    """
    # 超权
    # uid: 1 did: 1
    # uid: 2 did: 2
    # 要防止用户1去操作用户2的鱼漂
    with db.auto_commit():
        drift = Drift.query.filter_by(requester_id=current_user.id, id=did).first_or_404()
        # 将状态修改为 Redraw
        drift.pending = PendingStatus.Redraw.value
        # 返还鱼豆
        current_user.beans += 1

    return redirect(url_for('web.pending'))


@web.route('/drift/<int:did>/mailed')
@login_required
def mailed_drift(did):
    with db.auto_commit():
        drift = Drift.query.filter_by(gifter_id=current_user.id, id=did).first_or_404()
        # 将状态修改为 Success
        drift.pending = PendingStatus.Success.value
        # 获得一个鱼豆
        current_user.beans += 1
        # 修改礼物状态为完成
        gift = Gift.query.filter_by(id=drift.gift_id).first_or_404()
        gift.launched = True

        # 如果索要者存在对应未完成的心愿，也一并完成
        Wish.query.filter_by(isbn=drift.isbn, uid=drift.requester_id, launched=False).update({Wish.launched: True})

    return redirect(url_for('web.pending'))


def save_drift(drift_form, current_gift):
    pass


def save_to_drift(drift_form, current_gift):
    """
    保存鱼漂
    :param drift_form:
    :param current_gift:
    :return:
    """
    with db.auto_commit():
        drift = Drift()
        # drift.message = drift_form.message.data
        # populate_obj 方法将 form.data 中所有字段复制到目标对象下
        drift_form.populate_obj(drift)

        drift.requester_id = current_user.id
        drift.recipient_name = current_user.nickname
        drift.gifter_id = current_gift.user.id
        drift.gifter_name = current_gift.user.nickname
        drift.gift_id = current_gift.id

        book = BookViewModel(current_gift.book)

        drift.isbn = book.isbn
        drift.book_title = book.title
        drift.book_author = book.author
        drift.book_img = book.image

        current_user.beans -= 1

        db.session.add(drift)
