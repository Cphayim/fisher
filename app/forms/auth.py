# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 21:03
"""
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from models.user import User

__author__ = 'Cphayim'


class RegisterForm(Form):
    """
    注册表单验证
    """
    # 电子邮箱
    email = StringField(
        validators=[
            DataRequired(),
            Length(8, 64),
            Email(message='电子邮箱不符合规范')
        ]
    )

    # 密码
    password = PasswordField(
        validators=[
            DataRequired(message='密码不可以为空，请输入你的密码'),
            Length(6, 32)
        ]
    )

    # 昵称
    nickname = StringField(
        validators=[
            DataRequired(),
            Length(2, 10, message='昵称至少需要两个字符，最多10个字符')
        ]
    )

    # 自定义验证器，一定要以 validate_属性
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮箱已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('该昵称已被使用')


class LoginForm(Form):
    email = StringField(
        validators=[
            DataRequired(),
            Length(8, 64),
            Email()
        ]
    )

    password = PasswordField(
        validators=[
            DataRequired(),
            Length(6, 32)
        ]
    )
