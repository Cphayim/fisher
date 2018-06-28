# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/28 16:05
  鱼漂相关视图函数
"""
from . import web

__author__ = 'Cphayim'


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
def send_drift(gid):
    pass


@web.route('/pending')
def pending():
    pass


@web.route('/drift/<int:gid>/reject')
def reject_drift(gid):
    pass


@web.route('/drift/<int:gid>/redraw')
def redraw_drift(gid):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass


def save_drift(drift_form, current_gift):
    pass

