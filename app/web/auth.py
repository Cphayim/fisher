# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 16:00
  权限相关视图函数
"""
from . import web

__author__ = 'Cphayim'


@web.route('/register', methods=['GET', 'POST'])
def register():
    pass


@web.route('/login', methods=['GET', 'POST'])
def login():
    pass


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
