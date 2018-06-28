# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 16:21
"""
from . import web

__author__ = 'Cphayim'


@web.route('/set/cookie')
def set_cookie():
    pass


@web.route('/set/session')
def set_session():
    pass


@web.route('/get/session')
def get_session():
    pass
