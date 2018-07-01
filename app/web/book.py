# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/24 18:05
  书籍相关视图函数
"""
import json
import htmlmin

from flask import jsonify, request, render_template, flash
from flask_login import current_user

from forms.book import SearchForm
from libs.helper import is_isbn_or_key
from models.gift import Gift
from models.wish import Wish
from spider.yushu_book import YuShuBook
from view_models.book import BookCollection, BookViewModel
from models.book import Book
from view_models.trade import TradeInfo

from . import web

__author__ = 'Cphayim'


@web.route('/book/search')
def search():
    """
    书籍搜索视图函数
        q: 普通关键字或 isbn
        page
        ?q=xxx&page=xx
    """
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        # 判断当前关键字 q 是普通关键字还是 isbn 编号
        isbn_or_key = is_isbn_or_key(q)

        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        # return json.dumps(books, default=lambda o: o.__dict__), 200, {'content-type': 'application/json'}
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
        # return jsonify(form.errors)

    return htmlmin.minify(render_template('search_result.html', books=books, form=form),
                          remove_empty_space=True)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    """
    书籍详情视图函数
    业务逻辑：
        默认显示所有赠书人的名字
        确定当前用户是赠书人 -> 显示所有索要人的名字
        确定当前用户是索书人 -> 同默认
    :param isbn:
    :return:
    """
    #
    has_in_gifts = False
    has_in_wishes = False

    # 取书籍详情数据
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    # 如果当前有登录状态，查询该用户是否存在正在进行的赠/索书记录
    if current_user.is_authenticated:
        # 当前用户正在进行赠书
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True
        elif Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wishes = True

    # 查询该书所有正在进行的赠/索书记录
    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_model = TradeInfo(trade_gifts)
    trade_wishes_model = TradeInfo(trade_wishes)

    return render_template(
        'book_detail.html',
        book=book,
        gifts=trade_gifts_model,
        wishes=trade_wishes_model,
        has_in_gifts=has_in_gifts,
        has_in_wishes=has_in_wishes
    )

# @web.route('/test')
# def test():
#     r = {
#         'name': '',
#         'age': 18
#     }
#     flash('Hello, world', category='error')
#     flash('I\'m Cphayim', category='warning')
#     # 模板渲染
#     return render_template('test.html', data=r)
