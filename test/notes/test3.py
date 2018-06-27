# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/27 16:12
"""

import threading

__author__ = 'Cphayim'

print('I am Cphayim')


def worker():
    print('I am thread')
    t = threading.current_thread()
    print(t.getName())


new_t = threading.Thread(target=worker, name='q')
new_t.start()

# 主线程
t = threading.current_thread()
print(t.getName())

# 多核 CPU
# 可以同时并行的执行多个线程
# Python 没有办法充分利用多核 CPU 的优势 = =
# GIL（全局解释器锁 global interpreter lock） 机制导致 Python 不能使用多核 CPU
# 锁 线程安全

# 内存资源 一个进程 有多个线程 共享
# 可能同时要访问同一个资源
# 线程不安全

# 锁
# 细粒度锁 程序员 主动加锁
# 粗粒度锁 解释器 GIL 多个CPU 1个线程执行 一定程度上保证线程安全

# Python 的多线程在 CPU密集型程序 中用处不大，但在 IO密集型程序 中有很大用处