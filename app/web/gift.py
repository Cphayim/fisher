# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 16:12
"""
from flask import current_app, flash, url_for, redirect, render_template
from flask_login import login_required, current_user

from models.base import db
from models.gift import Gift
from view_models.gift import MyGifts
from . import web

__author__ = 'Cphayim'


@web.route('/my/gifts')
@login_required
def my_gifts():
    """
    赠送清单视图函数
    :return:
    """
    uid = current_user.id
    # 得到我的礼物列表
    gifts_of_mine = Gift.get_user_gifts(uid)
    # 每个礼物中的 isbn 编号组成的列表
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    # 获取每个 isbn 对应的心愿数量
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_model = MyGifts(gifts_of_mine, wish_count_list)
    return render_template('my_gifts.html', gifts=view_model.gifts)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    """
    保存赠书记录视图函数
    :param isbn:
    :return:
    """
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            # 每发起一次赠书，系统赠送用户鱼豆
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')

    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
