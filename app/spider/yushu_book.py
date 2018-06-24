# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/24 16:12
"""
from flask import current_app

from app.libs.httper import HTTP

__author__ = 'Cphayim'


class YuShuBook:
    # isbn API 请求地址
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    # keyword API 请求地址
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        """
        通过 isbn 请求数据
        :param isbn: isbn 编号
        :return:
        """
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        """
        通过关键字请求数据
        :param keyword: 关键字
        :param page: 页码
        :return:
        """
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = HTTP.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        """
        根据页码计算 start 参数
        :param page:
        :return:
        """
        return (page - 1) * current_app.config['PER_PAGE']
