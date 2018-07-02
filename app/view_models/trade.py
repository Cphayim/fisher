# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/2 00:58
"""
from view_models.book import BookViewModel

__author__ = 'Cphayim'


class TradeInfo:
    """
    交易信息
    """

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


class MyTrades:
    def __init__(self, trades_of_mine, trade_count_list):
        self.trades = []

        self.__trades_of_mine = trades_of_mine
        self.__trade_count_list = trade_count_list

        self.trades = self.__parse()

    def __parse(self):
        """
        解析数据，返回解析完毕的 trades
        :return:
        """
        temp_trades = []
        for trade in self.__trades_of_mine:
            my_trade = self.__matching(trade)
            temp_trades.append(my_trade)

        return temp_trades

    def __matching(self, trade):
        """
        返回一个 trade 对应的视图模型
        :param trade:
        :return:
        """
        count = 0
        for trade_count in self.__trade_count_list:
            if trade.isbn == trade_count['isbn']:
                count = trade_count['count']

        # my_gift = MyGift(gift.id, BookViewModel(gift.book), count)
        my_trade = {
            'id': trade.id,
            'book': BookViewModel(trade.book),
            'count': count
        }
        return my_trade
