# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/30 19:13
"""
from contextlib import contextmanager

__author__ = 'Cphayim'


class MyResource:

    def query(self):
        print('query data')


@contextmanager
def make_myresource():
    print('connect to resource')
    yield MyResource()
    print('close resource connection')


with make_myresource() as r:
    r.query()
