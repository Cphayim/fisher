# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/24 18:53
"""
from flask import Blueprint, render_template

__author__ = 'Cphayim'

# 创建蓝图实例
web = Blueprint('web', __name__)


@web.app_errorhandler(404)
def not_found(e):
    # AOP
    return render_template('404.html'), 404


from web import book, auth, drift, gift, main, wish, test
