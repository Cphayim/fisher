# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 20:22
"""
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, SmallInteger
from sqlalchemy.orm import relationship

from models.base import Base

__author__ = 'Cphayim'


class Gift(Base):
    """
    礼物（赠书）模型
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
