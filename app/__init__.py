# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/24 18:52
"""
from flask import Flask
from flask_login import LoginManager

from models.base import db

__author__ = 'Cphayim'

login_manager = LoginManager()


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
    login_manager.init_app(app)

    # db.create_all(app=app)
    with app.app_context():
        db.create_all()

    return app


def register_blueprint(app):
    """
    注册蓝图到 app
    :param app: 当前 app
    """
    from web import web
    app.register_blueprint(web)
