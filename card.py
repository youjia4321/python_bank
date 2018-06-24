# -*- coding:utf-8 -*-
__author__ = 'youjia'
__date__ = '2018/6/23 20:03'


class Card(object):  # 银行卡类
    def __init__(self, cardId, cardPasswd, cardMoney):
        self.cardId = cardId
        self.cardPasswd = cardPasswd
        self.cardMoney = cardMoney
        self.cardLock = False
