# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/25 01:01
"""
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

__author__ = 'Cphayim'

#
db = SQLAlchemy()


class Book(db.Model):
    # id
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 书名
    title = Column(String(50), nullable=False)
    # 作者
    author = Column(String(30), default='未名')
    # 装帧
    binding = Column(String(20))
    # 出版社
    publisher = Column(String(50))
    # 价格
    price = Column(String(20))
    # 页数
    pages = Column(Integer)
    # 出版时间
    pubdate = Column(String(20))
    # isbn 编号
    isbn = Column(String(15), nullable=False, unique=True)
    # 简介
    summary = Column(String(1000))
    # 封面
    image = Column(String(100))

    def sample(self):
        pass
