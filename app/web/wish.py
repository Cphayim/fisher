# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 16:25
"""
from flask import flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from libs.email import send_mail
from models.base import db
from models.gift import Gift
from models.wish import Wish
from view_models.trade import MyTrades
from . import web

__author__ = 'Cphayim'


def limit_key_prefix():
    pass


@web.route('/my/wish')
@login_required
def my_wish():
    uid = current_user.id
    # 得到我的心愿列表
    wishes_of_mine = Wish.get_user_wishes(uid)
    # 每个心愿中的 isbn 编号组成的列表
    isbn_list = [wish.isbn for wish in wishes_of_mine]
    gift_count_list = Wish.get_gift_counts(isbn_list)
    view_model = MyTrades(wishes_of_mine, gift_count_list)
    return render_template('my_wish.html', trades=view_model.trades)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    """
    保存到心愿清单
    :param isbn:
    :return:
    """
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')

    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
@login_required
def satisfy_wish(wid):
    wish = Wish.query.get_or_404(wid)
    gift = Gift.query.filter_by(uid=current_user.id, isbn=wish.isbn).first()
    # 如果该用户没有上传过此书，需要用户先将该书添加到礼物中
    if not gift:
        flash('你还没有上传此书'
              '请点击"加入到赠送清单"添加此书。添加之前，请确保自己可以赠送此书')
    else:
        send_mail(wish.user.email,
                  '有人想送你一本书',
                  'email/satisify_wish.html', wish=wish, gift=gift)
        flash('已向他/她发送了一封邮件，如果他/她愿意接受你的赠送，你将收到一个鱼漂')
    return redirect(url_for('web.book_detail', isbn=wish.isbn))


@web.route('/wish/book/<isbn>/redraw')
@login_required
def redraw_from_wish(isbn):
    """
    撤销心愿视图函数
    :param isbn: isbn
    :return:
    """
    wish = Wish.query.filter_by(isbn=isbn, launched=False).first_or_404()
    with db.auto_commit():
        wish.delete()

    return redirect(url_for('web.my_wish'))


def satifiy_with_limited():
    pass
