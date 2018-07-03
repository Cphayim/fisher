# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/24 22:30
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired, Regexp

__author__ = 'Cphayim'


class SearchForm(Form):
    """
    搜索表单验证
    """
    # 搜索关键字（普通关键字/isbn 编号）
    q = StringField(
        validators=[
            DataRequired(message='请填写关键字'),
            Length(min=1, max=30, message='关键字的长度应该在1-30位')
        ]
    )
    # 页码
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)


class DriftForm(Form):
    """
    鱼漂表单验证
    """
    # 收件人
    recipient_name = StringField(
        validators=[
            DataRequired('请填写收件人'),
            Length(min=2, max=20, message='收件人姓名长度必须在2-20个字符之间')
        ]
    )
    # 地址
    address = StringField(
        validators=[
            DataRequired('请填写地址'),
            Length(min=10, max=70, message='地址还不到10个字吗？尽量写详细一些吧')
        ]
    )
    # 手机号
    mobile = StringField(
        validators=[
            DataRequired('请填写手机号'),
            Regexp('^1\d{10}$', message='请输入正确的手机号')
        ]
    )
    # 留言消息
    message = StringField()
