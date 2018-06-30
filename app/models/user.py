# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 20:22
"""
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import login_manager
from models.base import Base

__author__ = 'Cphayim'


class User(UserMixin, Base):
    """
    用户模型
    """
    # 修改表名
    # __tablename__ = 'user1'
    # id
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 昵称
    nickname = Column(String(24), nullable=False)
    # 密码
    _password = Column('password', String(128), nullable=False)
    # 手机号码
    phone_number = Column(String(18), unique=True)
    # 邮箱
    email = Column(String(50), unique=True, nullable=False)
    # 是否确认邮箱
    confirmed = Column(Boolean, default=False)
    #
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    # getter
    @property
    def password(self):
        return self._password

    # setter
    @password.setter
    def password(self, raw):
        """
        设置一个加密密码
        :param raw: 明文密码
        :return:
        """
        self._password = generate_password_hash(raw)

    # 通过 get_id 方法返回一个唯一标识用来创建登录态 Cookie
    # 因为 UserMixin类 中的 get_id 方法默认返回的是 self.id
    # 所以此处不需要重写该方法
    # def get_id(self):
    #     return self.id

    def check_password(self, raw):
        """
        密码是否匹配
        :param raw: 明文密码
        :return:
        """
        return check_password_hash(self.password, raw)


# @login_required 装饰的视图函数需要用到
@login_manager.user_loader
def get_user(uid):
    """
    通过 uid 查询用户对象并返回
    :param uid:
    :return:
    """
    # 查询主键使用 get
    return User.query.get(int(uid))
