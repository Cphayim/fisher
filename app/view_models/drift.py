# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/4 09:20
"""
from libs.enums import PendingStatus

__author__ = 'Cphayim'


class DriftViewModel:
    def __init__(self, drift, current_user_id):
        self.data = {}

        self.data = self.__parse(drift, current_user_id)

    def __parse(self, drift, current_user_id):
        """
        解析数据
        :param drift:
        :param current_user_id:
        :return:
        """
        you_are = self.requester_or_gifter(drift, current_user_id)
        # 枚举中返回状态文字
        pending_status = PendingStatus.pending_str(drift.pending, you_are)
        r = {
            'drift_id': drift.id,
            'book_title': drift.book_title,
            'book_author': drift.book_author,
            'book_img': drift.book_img,
            'date': drift.create_datetime.strftime('%Y-%m-%d'),
            'message': drift.message,
            'address': drift.address,
            'recipient_name': drift.recipient_name,
            'mobile': drift.mobile,
            'status': drift.pending,
            'you_are': you_are,
            'operator': drift.recipient_name if you_are != 'requester' else drift.gifter_name,
            'status_str': pending_status
        }
        return r

    @staticmethod
    def requester_or_gifter(drift, current_user_id):
        """
        判断是索要者还是赠送者
        :param drift:
        :param current_user_id:
        :return:
        """
        # 不建议在这里导入使用 current_user（强耦合）
        if drift.requester_id == current_user_id:
            you_are = 'requester'
        else:
            you_are = 'gifter'
        return you_are


class DriftCollection:
    def __init__(self, drifts, current_user_id):
        self.data = []

        self.__paser(drifts, current_user_id)

    def __paser(self, drifts, current_user_id):
        for drift in drifts:
            temp = DriftViewModel(drift, current_user_id)
            self.data.append(temp.data)
