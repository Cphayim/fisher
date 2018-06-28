# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 00:23
"""

__author__ = 'Cphayim'


class BookViewModel:
    """
    书籍类
    """
    def __init__(self, book):
        # 书名
        self.title = book['title']
        # 出版社
        self.publisher = book['publisher']
        # 页数
        self.pages = book['pages'] or ''
        # 作者
        self.author = '、'.join(book['author'])
        # 价格
        self.price = book['price']
        # 简介
        self.summary = book['summary'] or ''
        # 封面图
        self.image = book['image']


class BookCollection:
    """
    书籍集合类
    用于响应的视图模型
    """
    def __init__(self):
        # 总数
        self.total = 0
        # 书籍列表
        self.books = []
        # 搜索关键字
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        """
        填充数据到对象
        :param yushu_book:
        :param keyword:
        :return:
        """
        self.total = yushu_book.total
        self.keyword = keyword
        # 通过 yushu_book 对象中的 books 列表创建 BookViewModel 组成的列表
        self.books = [BookViewModel(book) for book in yushu_book.books]


"""
已废弃
"""
class _BookViewModel:

    # 描述特征（类变量、实例变量）
    # 行为（方法）
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
