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

    @classmethod
    def pending_str(cls, status, key):
        key_map = {
            cls.Waiting.value: {
                'requester': '等待对方邮寄',
                'gifter': '等待你邮寄'
            },
            cls.Success.value: {
                'requester': '对方已邮寄',
                'gifter': '你已邮寄，交易完成'
            },
            cls.Reject.value: {
                'requester': '对方已拒绝',
                'gifter': '你已拒绝'
            },
            cls.Redraw.value: {
                'requester': '你已撤销',
                'gifter': '对方已撤销'
            }
        }
        return key_map[status][key]
