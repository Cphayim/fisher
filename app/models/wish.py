# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/30 18:11
"""
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, desc, func
from sqlalchemy.orm import relationship

from models.base import Base, db
from spider.yushu_book import YuShuBook

__author__ = 'Cphayim'


class Wish(Base):
    """
    心愿清单（索书）模型
    """
    # id
    id = Column(Integer, primary_key=True)
    # 用户
    user = relationship('User')
    # 用户 id（外键）
    uid = Column(Integer, ForeignKey('user.id'))
    # isbn 编号
    isbn = Column(String(15), nullable=False)
    # 是否已收到
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        """
        通过 isbn 请求书籍信息
        返回 yushu_book.first
        :return:
        """
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def get_user_wishes(cls, uid):
        """
        获取用户的心愿列表
        :return:
        """
        wishes = Wish.query.filter_by(uid=uid, launched=False) \
            .order_by(desc(Wish.create_time)) \
            .all()

        return wishes

    @classmethod
    def get_gift_counts(cls, isbn_list):
        """
        根据传入的一组 isbn，到 Gift 表中计算出某个礼物的 Gift 赠送数量
        返回一个 {'count': xxx, 'isbn': xxx} 字典组成的列表
        :return:
        """
        from models.gift import Gift
        count_list = db.session.query(func.count(Gift.id), Gift.isbn) \
            .filter(Gift.isbn.in_(isbn_list), Gift.launched == False, Gift.status == 1) \
            .group_by(Gift.isbn) \
            .all()

        # 应该返回字典结构而非元组结构
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list
