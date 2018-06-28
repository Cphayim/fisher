# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/24 18:05
"""
import json

from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel, BookCollection
from . import web

__author__ = 'Cphayim'


# 创建蓝图对象
@web.route('/book/search')
def search():
    """
    书籍搜索视图函数
        q: 普通关键字或 isbn
        page
    """
    form = SearchForm(request.args)

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        # 判断当前关键字 q 是普通关键字还是 isbn 编号
        isbn_or_key = is_isbn_or_key(q)

        yushu_book = YuShuBook()
        books = BookCollection()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        return json.dumps(books, default=lambda o: o.__dict__), 200, {'content-type': 'application/json'}
    else:
        return jsonify(form.errors)
