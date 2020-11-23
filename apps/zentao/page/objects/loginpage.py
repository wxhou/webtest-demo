#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from config.conf import element
from utils.times import sleep
from common.readelemnts import Element
from apps.zentao.page import BasePage

login = Element(element['zentao'], 'login')
home = Element(element['zentao'], 'home')


class LoginPage(BasePage):
    def login(self, user, pwd):
        self.input_text(login['账号'], text=user)
        self.input_text(login['密码'], text=pwd)
        self.is_click(login['登录'])
        sleep(3)

    def quit_login(self):
        self.is_click(login['用户头像'])
        self.is_click(login['注销'])


if __name__ == "__main__":
    print(login['密码'])
