# -*- coding:utf-8 -*-
__author__ = 'youjia'
__date__ = '2018/6/23 19:15'

import time


class Admin(object):
    admin = '1'
    password = '1'

    def adminView(self):
        print('...............................................................')
        print('.                                                             .')
        print('.                       欢迎来到家鸽银行                         .')
        print('...............................................................')



    def sysFunctionView(self):
        print('''
...............................................................
.   开户(1)                           查询(2)                   #
.   取款(3)                           存款(4)                   #
.   转账(5)                           改密(6)                   #
.   锁定(7)                           解锁(8)                   #
.   补卡(9)                           销户(0)                   #                                                            
.          退出(q)                后台(a)                       #
...............................................................
        ''')

    def adminLogin(self):
        inputAdmin = input('请输入管理员账号：')
        if self.admin != inputAdmin:
            print('账号输入有误!!')
            return -1
        inputPasswd = input('请输入管理员密码：')
        if self.password != inputPasswd:
            print('密码输入有误!!')
            return -1
        print('操作成功，请稍后....')
        time.sleep(2)
        return 0
