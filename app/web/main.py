# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 16:17
"""
from flask import render_template

from models.gift import Gift
from view_models.book import BookViewModel
from . import web

__author__ = 'Cphayim'


@web.route('/')
def index():
    """
    首页视图函数
    :return:
    """
    recent_gift = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gift]
    return render_template('index.html', recent=books)


@web.route('/personal')
def personal_center():
    pass
