#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from tools.times import sleep
from page.webpage import WebPage
from common.readelemnts import Element

login = Element('login')
home = Element('home')


class LoginPage(WebPage):
    def login(self, user, pwd):
        self.input_text(login['账号'], text=user)
        self.input_text(login['密码'], text=pwd)
        self.is_click(login['登录'])
        sleep(3)

    def quit_login(self):
        self.is_click(login['用户头像'])
        self.is_click(login['注销'])


if __name__ == "__main__":
    pass
