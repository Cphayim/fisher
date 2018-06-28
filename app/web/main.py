# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 16:17
"""
from . import web

__author__ = 'Cphayim'

@web.route('/')
def index():
    pass

@web.route('/personal')
def personal_center():
    pass