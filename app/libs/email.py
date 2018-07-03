# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/3 09:46
"""
from flask import current_app, render_template
from flask_mail import Message

from app import mail

__author__ = 'Cphayim'


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
    mail.send(msg)
