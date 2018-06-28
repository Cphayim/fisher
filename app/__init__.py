# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/24 18:52
"""
from flask import Flask

from models.base import db
from web import web

__author__ = 'Cphayim'


def create_app():
    """
    创建 app 实例
    """
    app = Flask(__name__)

    # 添加配置
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')

    # 注册蓝图
    register_blueprint(app)

    # 添加插件
    db.init_app(app)

    # db.create_all(app=app)
    with app.app_context():
        db.create_all()

    return app


def register_blueprint(app):
    """
    注册蓝图到 app
    :param app: 当前 app
    """
    app.register_blueprint(web)
