# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/24 18:05
"""
from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
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

        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)

        return jsonify(result)

    else:
        return jsonify(form.errors)
