# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 16:00
  权限相关视图函数
"""
from flask import render_template, request, redirect, url_for
from forms.auth import RegisterForm, LoginForm
from models.base import db
from models.user import User

from . import web

__author__ = 'Cphayim'


@web.route('/register', methods=['GET', 'POST'])
def register():
    """
    用户注册视图函数
    :return:
    """
    form = RegisterForm(request.form)

    # 处理注册表单提交
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))

    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    """
    用户登录视图函数
    :return:
    """
    form = LoginForm(request.form)

    # 处理登录表单提交
    if request.method == 'POST' and form.validate():
        pass

    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


# 单元测试
@web.route('/rest/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
