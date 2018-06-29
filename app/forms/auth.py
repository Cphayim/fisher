# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 21:03
"""
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from models.user import User

__author__ = 'Cphayim'


class LoginForm(Form):
    """
    登录表单验证器
    """
    # 电子邮箱
    email = StringField(
        validators=[
            DataRequired(message='电子邮箱不可以为空'),
            Length(8, 64, message='电子邮箱不符合规范'),
            Email(message='电子邮箱不符合规范')
        ]
    )

    # 密码
    password = PasswordField(
        validators=[
            DataRequired(message='密码不可以为空'),
            Length(6, 32, message='密码长度应该在6~32位')
        ]
    )


class RegisterForm(LoginForm):
    """
    注册表单验证器
    """

    # 昵称
    nickname = StringField(
        validators=[
            DataRequired('昵称不可以为空'),
            Length(2, 10, message='昵称长度应该在2~10个字符')
        ]
    )

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('该昵称已被使用')

    # 自定义验证器，一定要以 validate_属性
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮箱已被注册')
