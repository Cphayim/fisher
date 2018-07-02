# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 20:22
"""
from flask import current_app
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc
from sqlalchemy.orm import relationship

from models.base import Base
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
