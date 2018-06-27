# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 00:23
"""

__author__ = 'Cphayim'


class BookViewModel:

    @classmethod
    def package_sigle(cls, data, keyword):
        """
        处理单本书籍搜索的数据（isbn 查找）
        :param data: 原数据
        :param keyword: 搜索关键字
        :return:
        """
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }

        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]

        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        """
        处理搜索列表的数据（关键字查找）
        :param data: 原数据
        :param keyword: 搜索关键字
        :return:
        """
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }

        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]

        return returned

    @classmethod
    def __cut_book_data(cls, data):
        """
        裁剪书籍数据
        :param data: 数据信息原数据
        :return:
        """
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
