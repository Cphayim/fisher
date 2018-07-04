# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 20:23
"""
from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, Integer, SmallInteger

__author__ = 'Cphayim'


# 继承原 flask-sqlalchemy 的 SQLAlchemy 类，实现 auto_commit
class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        """
        自动执行提交的上下文管理器
        :return:
        """
        try:
            yield
            # 事务
            # with 语句块内代码执行完毕后自动 commit
            self.session.commit()
        except Exception as e:
            # 若插入出现异常，执行回滚
            self.session.rollback()
            raise e


# 继承 flask-sqlalchemy 的 BaseQuery 类，重写 filter_by 方法
class Query(BaseQuery):
    def filter_by(self, **kwargs):
        """
        自定义 filter_by，查询未被标记删除的数据
        :param kwargs:
        :return:
        """
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1

        return super(Query, self).filter_by(**kwargs)


# 初始化 SQLAlchemy，指定自定义的 Query 类
db = SQLAlchemy(query_class=Query)


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

    def delete(self):
        """
        标记删除数据
        :return:
        """
        self.status = 0

    @property
    def create_datetime(self):
        """
        转换为时间对象的 create_time
        :return:
        """
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None
