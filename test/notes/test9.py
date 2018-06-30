# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/30 19:22
"""
from contextlib import contextmanager

__author__ = 'Cphayim'


@contextmanager
def book_mark():
    print('《', end='')
    yield
    print('》', end='')


with book_mark():
    print('且将生活一饮而尽', end='')
