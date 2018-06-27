# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/27 23:51
"""

__author__ = 'Cphayim'

# 以线程 ID 号作为 key 的字典 -> Local -> LocalStack

# AppContext RequestContext -> LocalStack

# Flask -> AppContext     Request -> RequestContext

# current_app -> (LocalStack.top = AppContext top.app=Flask)

# request -> (LocalStack.top = RequestContext top.request=Request)