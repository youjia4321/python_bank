# -*- coding:utf-8 -*-
__author__ = 'youjia'
__date__ = '2018/6/23 20:03'


class User(object):  # 用户类
    def __init__(self, name, idCard, phone, card):
        self.name = name
        self.idCard = idCard
        self.phone = phone
        self.card = card
