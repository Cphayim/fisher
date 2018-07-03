# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/3 16:24
"""

__author__ = 'Cphayim'

from enum import Enum


class PendingStatus(Enum):
    """
    交易的状态
    """
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4
