# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 20:23
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

__author__ = 'Cphayim'

# 初始化 SQLAlchemy
db = SQLAlchemy()


class Base(db.Model):
    """
    模型基类
    """
    __abstract__ = True
    # 创建时间
    create_time = Column('create_time', Integer)
    # 当前状态 1: 存在
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        """
        动态为对象设置属性
        传入一个字典，将与字典中有同名的 key 的值赋给对象的属性
        :param attrs_dict:
        :return:
        """
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
