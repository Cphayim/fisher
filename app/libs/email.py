# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/3 09:46
"""
from threading import Thread

from flask import current_app, render_template
from flask_mail import Message

from app import mail

__author__ = 'Cphayim'


def send_async_mail(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_mail(to, subject, template, **kwargs):
    """
    发送电子邮件
    :param to: 目标电子邮箱
    :param subject: 标题
    :param template: 使用的 html 模板路径
    :param kwargs: 渲染数据
    :return:
    """
    msg = Message(
        current_app.config.get('MAIL_SUBJECT_PREFIX', '') + subject,
        sender=current_app.config.get('MAIL_USERNAME'),
        recipients=[to]
    )
    msg.html = render_template(template, **kwargs)

    app = current_app._get_current_object()
    # 启动一个线程来发送邮件
    thr = Thread(target=send_async_mail, args=[app, msg])
    thr.start()
