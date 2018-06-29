# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/24 16:12
"""
from flask import current_app

from libs.httper import HTTP

__author__ = 'Cphayim'


class YuShuBook:
    # isbn API 请求地址
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    # keyword API 请求地址
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        # 总数
        self.total = 0
        # 书籍列表
        self.books = []

    def search_by_isbn(self, isbn):
        """
        通过 isbn 请求数据
        :param isbn: isbn 编号
        :return:
        """
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=1):
        """
        通过关键字请求数据
        :param keyword: 关键字
        :param page: 页码
        :return:
        """
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.__calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def __fill_single(self, data):
        """
        数据填充-单书籍（isbn 搜索）
        :param data:
        :return:
        """
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        """
        数据填充-书籍列表（关键字 查找）
        :param data:
        :return:
        """
        self.total = data['total']
        self.books = data['books']

    @staticmethod
    def __calculate_start(page):
        """
        根据页码计算 start 参数
        :param page:
        :return:
        """
        return (page - 1) * current_app.config['PER_PAGE']

    @property
    def first(self):
        """
        返回 books 第一个 book 对象
        :return:
        """
        return self.books[0] if self.total >= 1 else None
