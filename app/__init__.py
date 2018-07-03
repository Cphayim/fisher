# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/24 18:52
"""
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail

from models.base import db

__author__ = 'Cphayim'

login_manager = LoginManager()
mail = Mail()

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

    # 初始化 flask-sqlalchemy
    db.init_app(app)

    # 根据模型创建数据表（model 在 web 中引用）
    # db.create_all(app=app)
    with app.app_context():
        db.create_all()

    # 初始化 flask-login
    login_manager.init_app(app)
    # 指定登录视图函数的 endpoint 和 提示消息
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    # 初始化 flask-mail
    mail.init_app(app)

    return app


def register_blueprint(app):
    """
    注册蓝图到 app
    :param app: 当前 app
    """
    # web 所引用的模块需要使用到 login_manager 对象
    # 所以在注册蓝图时再引入 web
    from web import web
    app.register_blueprint(web)
