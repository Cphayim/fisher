# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 20:23
"""
from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

__author__ = 'Cphayim'


# SQLAlchemy 的子类，实现一个自动 commit 的上下文管理器
class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            # 事务
            # with 语句块内代码执行完毕后自动 commit
            self.session.commit()
        except Exception as e:
            # 若插入出现异常，执行回滚
            self.session.rollback()
            raise e


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

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

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
