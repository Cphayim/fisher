# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/27 17:52
"""

__author__ = 'Cphayim'

from werkzeug.local import Local, LocalStack

# 原理 字典 保存数据
# 操作数据
# werkzeug local Local 字典
# Local 使用字典的方式实现的线程隔离
# LocalStack 线程隔离的栈结构
# 封装 没有什么是封装解决不了的 如果一次封装解决不了问题，那么就再来一次

s = LocalStack()
s.push(1)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

s.push(1)
s.push(2)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)