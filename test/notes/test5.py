# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/27 23:20
"""
import threading
import time

from werkzeug.local import LocalStack

__author__ = 'Cphayim'

my_stack = LocalStack()
my_stack.push(1)
print('in main thread after push, value is: ' + str(my_stack.top))


def worker():
    # 新线程
    print('in new thread before push, value is: ' + str(my_stack.top))
    my_stack.push(2)
    print('in new thread after push, value is: ' + str(my_stack.top))

new_t = threading.Thread(target=worker, name='q')
new_t.start()
time.sleep(1)
# 主线程
print('finally, in main thread value is: '+ str(my_stack.top))
