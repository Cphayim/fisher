# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/2 17:00
"""
from collections import namedtuple

from view_models.book import BookViewModel

__author__ = 'Cphayim'


# 通过 namedtuple 快速定义一个只包含构造函数和实例变量的类
# MyGift = namedtuple('MyGift', ['id', 'book', 'wishes_count'])


class MyGifts:
    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []

        self.__gift_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list

        self.gifts = self.__parse()

    def __parse(self):
        """
        解析数据，返回解析完毕的 gifts
        :return:
        """
        temp_gifts = []
        for gift in self.__gift_of_mine:
            my_gift = self.__matching(gift)
            temp_gifts.append(my_gift)

        return temp_gifts

    def __matching(self, gift):
        """
        返回一个 gift 对应的视图模型
        :param gift:
        :return:
        """
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']

        # my_gift = MyGift(gift.id, BookViewModel(gift.book), count)
        my_gift = {
            'id': gift.id,
            'book': BookViewModel(gift.book),
            'wishes_count': count
        }
        return my_gift
