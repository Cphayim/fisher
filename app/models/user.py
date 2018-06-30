# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 20:22
"""
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import login_manager
from libs.helper import is_isbn_or_key
from models.base import Base
from models.gift import Gift
from models.wish import Wish
from spider.yushu_book import YuShuBook

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
    # 鱼豆
    beans = Column(Float, default=0)
    # 赠书数
    send_counter = Column(Integer, default=0)
    # 索书数
    receive_counter = Column(Integer, default=0)
    # 微信 open_id
    wx_open_id = Column(String(50))
    # 微信名
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

    def can_save_to_list(self, isbn):
        """
        判断能否保存赠/索书记录
        :param isbn:
        :return:
        """
        if is_isbn_or_key(isbn) != 'isbn':
            return False

        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False

        # 不允许一个用户同时赠送多本相同的图书
        # 一个用户不可能同时成为赠送者和索要者（逻辑上冲突）

        # 既不在赠送清单，又不在心愿清单才能添加
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()

        if not gifting and not wishing:
            return True
        else:
            return False


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
