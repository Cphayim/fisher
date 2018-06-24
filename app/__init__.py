# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/24 18:52
"""
from flask import Flask

from app import setting, secure
from app.web import web

__author__ = 'Cphayim'


def create_app():
    """
    创建 app 实例
    """
    app = Flask(__name__)
    app.config.from_object(setting)
    app.config.from_object(secure)
    register_blueprint(app)
    return app


def register_blueprint(app):
    """
    注册蓝图到 app
    :param app: 当前 app
    """
    app.register_blueprint(web)
