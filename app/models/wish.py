# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/30 18:11
"""
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

from models.base import Base

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
