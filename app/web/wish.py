# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 16:25
"""
from . import web

__author__ = 'Cphayim'


def limit_key_prefix():
    pass


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    pass


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass

def satifiy_with_limited():
    pass