# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/24 18:05
  书籍相关视图函数
"""
import json
import htmlmin

from flask import jsonify, request, render_template, flash

from forms.book import SearchForm
from libs.helper import is_isbn_or_key
from spider.yushu_book import YuShuBook
from view_models.book import BookCollection, BookViewModel
from models.book import Book

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
    :param isbn:
    :return:
    """
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    return render_template('book_detail.html', book=book, wishes=[], gifts=[])

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
