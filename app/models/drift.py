# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/3 14:22
"""
from sqlalchemy import Column, Integer, String, SmallInteger

from models.base import Base

__author__ = 'Cphayim'


class Drift(Base):
    """
    鱼漂数据模型
    一次具体的交易信息
    """
    id = Column(Integer, primary_key=True)

    # 邮寄信息
    # 收件人
    recipient_name = Column(String(20), nullable=False)
    # 地址
    address = Column(String(150), nullable=False)
    # 留言消息
    message = Column(String(300))
    # 联系电话
    mobile = Column(String(20), nullable=False)

    # 书籍信息
    # isbn 编号
    isbn = Column(String(13))
    # 书名
    book_title = Column(String(50))
    # 作者
    book_author = Column(String(30))
    # 书籍封面
    book_img = Column(String(50))

    # 下面的信息不使用外键关联，是因为交易信息属于历史数据

    # 请求者信息
    # 请求者 id
    requester_id = Column(Integer)
    # 请求者昵称
    requester_nickname = Column(String(20))

    # 赠送者信息
    # 赠送者 id
    gifter_id = Column(Integer)
    # 赠送者昵称
    gifter_name = Column(Integer)
    # 礼物 id
    gift_id = Column(Integer)

    # 状态 libs/enums.py -> PendingStatus
    pending = Column('pending', SmallInteger, default=1)
