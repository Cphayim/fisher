# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/24 18:53
"""
from flask import Blueprint

__author__ = 'Cphayim'

# 创建蓝图实例
web = Blueprint('web', __name__)

from web import book, auth, drift, gift, main, wish, test
