# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 16:12
"""
from . import web

__author__ = 'Cphayim'


@web.route('/my/gifts')
def my_gifts():
    pass


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
