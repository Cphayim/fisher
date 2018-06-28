# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/24 22:30
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired

__author__ = 'Cphayim'


class SearchForm(Form):
    """
    搜索表单验证
    """
    # 搜索关键字（普通关键字/isbn 编号）
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    # 页码
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
