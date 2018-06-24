# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/24 15:41
"""

__author__ = 'Cphayim'


def is_isbn_or_key(word):
    """
    判断 word 参数是普通关键字还是 isbn 编号

    :param word: 关键字
    :return:
    """
    # isbn13 13个0到9的数字组成
    # isbn10 10个0到9的数字组成，含有一些 '-'
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'

    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key
