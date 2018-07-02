# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 20:22
"""

from flask import current_app
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc, func
from sqlalchemy.orm import relationship

from models.base import Base, db
from models.wish import Wish
from spider.yushu_book import YuShuBook

__author__ = 'Cphayim'


class Gift(Base):
    """
    赠送清单（赠书）模型
    """
    # id
    id = Column(Integer, primary_key=True)
    # 用户
    user = relationship('User')
    # 用户 id（外键）
    uid = Column(Integer, ForeignKey('user.id'))
    # 数据库中没有存 book 的数据（数据来自鱼书API）
    # book = relationship(Book)
    # bid = Column(Integer, ForeignKey('book.id'))
    # isbn 编号
    isbn = Column(String(15), nullable=False)
    # 是否已送出
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        """
        通过 Gift 对象的 isbn 请求书籍信息
        返回 yushu_book.first
        :return:
        """
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    # 这里使用 classmethod 比较合适
    # Gift 的对象代表一个礼物，具体
    # Gift 类代表礼物这个事物，它是抽象，不是具体的"一个"
    @classmethod
    def recent(cls):
        """
        查询最近的礼物
        显示一定数量（按照配置项 RECENT_BOOK_COUNT）
        时间倒叙排列
        去重（按照书籍）
        :return:
        """
        recent_gift = Gift.query.filter_by(launched=False) \
            .group_by(Gift.isbn) \
            .order_by(desc(Gift.create_time)) \
            .limit(current_app.config['RECENT_BOOK_COUNT']) \
            .distinct() \
            .all()

        return recent_gift

    @classmethod
    def get_user_gifts(cls, uid):
        """
        获取用户的礼物列表
        :return:
        """
        gifts = Gift.query.filter_by(uid=uid, launched=False) \
            .order_by(desc(Gift.create_time)) \
            .all()

        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        """
        根据传入的一组 isbn，到 Wish 表中计算出某个礼物的 Wish 心愿数量
        返回一个 {'count': xxx, 'isbn': xxx} 字典组成的列表
        :return:
        """
        # filter 接收的是条件表达式
        # mysql in
        # 我们要的是一组数量
        count_list = db.session.query(func.count(Wish.id), Wish.isbn) \
            .filter(Wish.isbn.in_(isbn_list), Wish.launched == False, Wish.status == 1) \
            .group_by(Wish.isbn) \
            .all()

        # 应该返回字典结构而非元组结构
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list
