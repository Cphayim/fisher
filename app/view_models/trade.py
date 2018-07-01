# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/2 00:58
"""

__author__ = 'Cphayim'


class TradeInfo:
    def __init__(self, goods):
        # 总数
        self.total = 0
        # 数据
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self, single):
        """
        数据转换
        :param single:
        :return:
        """
        if single.create_datetime:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'

        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )
