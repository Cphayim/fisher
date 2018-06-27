# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/25 21:47
"""

__author__ = 'Cphayim'

from flask import Flask, current_app, request, Request

app = Flask(__name__)

# 上下文的本质是对象
# 对一系列 flask 的对象进行封装
# 应用上下文 对象：提供对 Flask 这个类的核心对象的封装
# 请求上下文 对象：提供对 Request 的封装
# 在这些封装之上提供了一些方法
# Flask AppContext
# Request RequestContext
# 离线应用、单元测试 需要手动将 RequestContext 推入 _request_context_stack

# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()
# b = current_app

# with ctx_expression as var:
# ctx_expression -> 上下文表达式，必须返回一个上下文管理器
# with app.app_context():
#     a = current_app
#     d = current_app.config['DEBUG']

# 对一个实现了上下文协议的对象使用 with 语句
# 对于实现了上下文协议的对象，通常称为上下文管理器
# __enter__ __exit__

# with open(r'') as f:
#     f.read()


class MyResource:

    def __enter__(self):
        print('connect to resource')
        return self

    # __exit__ 方法用于回收资源和处理异常
    # 返回一个 bool 值来代表是否已妥善处理了异常
    # 若返回 False，代表 __exit__ 中未完成异常处理，异常将再次向外抛出
    # 若返回 True，代表 __exit__ 中已经完成异常处理，不会向外抛出
    # 若都不返回将等同于返回 False
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print('process exception')
        else:
            print('no exception')
        print('close resource connection')
        return False

    def query(self):
        print('query data')


with MyResource() as resource:
    1/0
    resource.query()

print(1)