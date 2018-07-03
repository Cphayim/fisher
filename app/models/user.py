# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 20:22
"""
from math import floor

from flask import current_app
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app import login_manager
from libs.enums import PendingStatus
from libs.helper import is_isbn_or_key
from models.base import Base, db
from models.drift import Drift
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

    def can_send_drift(self):
        """
        是否能发起鱼漂
        :return:
        """
        # 鱼豆必须足够（大于等于1）
        if self.beans < 1:
            return False
        # 成功送出的总数
        success_gifts_count = Gift.query.filter_by(uid=self.id, launched=True).count()
        # 成功收到的总数
        success_receive_count = Drift.query.filter_by(requester_id=self.id, pending=PendingStatus.Success).count()

        # 每索取两本书，自己必须送出一本书
        return True if \
            floor(success_receive_count / 2) <= floor(success_gifts_count) \
            else False

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

    def generate_token(self, expiration=600):
        """
        生成 token
        :param expiration: token 有效期
        :return:
        """
        s = Serializer(current_app.config.get('SECRET_KEY'), expiration)
        # s.dumps 返回一个二进制的密文，需要解码
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def reset_password(token, new_password):
        """
        重置密码
        :param token: token
        :param new_password: 新密码
        :return:
        """
        s = Serializer(current_app.config.get('SECRET_KEY'))
        try:
            # 需要将 str 编码为 二进制
            data = s.loads(token.encode('utf-8'))
        except:
            return False

        uid = data.get('id')
        with db.auto_commit():
            user = User.query.get(uid)
            user.password = new_password

        return True

    @property
    def summary(self):
        """
        用户简介
        :return:
        """
        return dict(
            nickname=self.nickname,
            beans=self.beans,
            email=self.email,
            send_receive=str(self.send_counter) + '/' + str(self.receive_counter)
        )


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
