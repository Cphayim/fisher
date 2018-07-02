# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 16:25
"""
from flask import flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from models.base import db
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
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass


def satifiy_with_limited():
    pass
