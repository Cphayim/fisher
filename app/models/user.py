# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 20:22
"""
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash

from models.base import Base

__author__ = 'Cphayim'


class User(Base):
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
    _password = Column('password', String(128))
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
        self._password = generate_password_hash(raw)
