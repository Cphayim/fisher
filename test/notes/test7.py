# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/30 19:04
"""

__author__ = 'Cphayim'


# 普通上下文管理器
class MyResource:

    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('close resource connection')

    def query(self):
        print('query data')


with MyResource() as r:
    r.query()