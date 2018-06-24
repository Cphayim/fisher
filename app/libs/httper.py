# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/24 15:48
"""

__author__ = 'Cphayim'

import requests


# urllib 原生
# requests 第三方

class HTTP:

    @staticmethod
    def get(url, return_json=True):
        """
        发起一个 HTTP GET 请求
        :param url: 请求地址
        :param return_json: 是否返回 JSON 对象（解析后）
        :return:
        """
        r = requests.get(url)

        # 处理 HTTP 响应状态码非 200 的情况
        if r.status_code != 200:
            return {} if return_json else ''

        return r.json() if return_json else r.text