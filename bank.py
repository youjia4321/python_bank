# -*- coding:utf-8 -*-
__author__ = 'youjia'
__date__ = '2018/6/23 19:37'
from admin import Admin
from atm import ATM
import pickle
import os
import time


def main():
    admin = Admin()
    admin.adminView()
    if admin.adminLogin():
        return -1
    path = os.path.join(os.getcwd(), 'allUsers.txt')
    # f = open(path, 'rb')
    # allUsers = pickle.load(f)
    allUsers = {}
    atm = ATM(allUsers)

    while True:
        admin.sysFunctionView()
        # 等待用户的操作
        option = input('请选择业务：')
        if option == '1':
            atm.createUser()
        elif option == '2':
            atm.searchInfo()
        elif option == '3':
            atm.getMoney()
        elif option == '4':
            atm.saveMoney()
        elif option == '5':
            atm.transferMoney()
        elif option == '6':
            atm.changePasswd()
        elif option == '7':
            atm.lockUser()
        elif option == '8':
            atm.unlockUser()
        elif option == '9':
            atm.report()
        elif option == '0':
            atm.destory()
        elif option == 'q':
            if not admin.adminLogin():
                path = os.path.join(os.getcwd(), 'allUsers.txt')
                f = open(path, 'wb')
                pickle.dump(atm.allUsers, f)
                f.close()
                return -1
        elif option == 'a':
            atm.admin()

        time.sleep(2)


if __name__ == '__main__':
    main()
