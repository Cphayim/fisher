# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 16:00
  权限相关视图函数
"""
from flask import render_template, request, redirect, url_for, flash, current_app
from flask_login import login_user, logout_user

from forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from models.base import db
from models.user import User
from libs.email import send_mail

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
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)

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

        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            # remember 参数确定用户登录的 cookie 是否持久保存
            # 默认为 False，退出浏览器即删除
            # 设置为 True 时，默认保存 365 天，具体配置 http://www.pythondoc.com/flask-login/#cookie
            login_user(user, remember=True)
            # 获取要跳转的地址
            next = request.args.get('next')
            # next 不是以 '/' 开头，也返回首页（防止重定向攻击）
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误')

    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    """
    忘记密码申请视图函数
    :return:
    """
    form = EmailForm(request.form)
    if request.method == 'POST' and form.validate():
        account_email = form.email.data
        user = User.query.filter_by(email=account_email).first_or_404()
        # 向用户发送电子邮件
        send_mail(
            account_email, '重置你的密码', 'email/reset_password.html',
            user=user, token=user.generate_token()
        )
        flash('一封邮件已发送到邮箱' + account_email + ', 请及时查收')
        # return redirect(url_for('web.login'))

    return render_template('auth/forget_password_request.html', form=form)


@web.route('/rest/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    """
    忘记密码视图函数
    :param token:
    :return:
    """
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        success = User.reset_password(token, form.password1.data)

        if success:
            flash('你的密码已经更新，请使用新密码登录')
            return redirect(url_for('web.login'))
        else:
            flash('密码重置失败')

    return render_template('auth/forget_password.html', form=form)


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    """
    用户登出（注销）视图函数
    :return:
    """
    logout_user()
    return redirect(url_for('web.index'))
