#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from utils.times import sleep
from Page.webpage import WebPage
from common.readelemnts import Element

login = Element('login')
home = Element('home')


class LoginPage(WebPage):
    def login(self, user, pwd):
        self.input_text(login['账号'], text=user)
        self.input_text(login['密码'], text=pwd)
        self.click_element(login['登录'])
        sleep()

    def quit_login(self):
        self.click_element(login['用户头像'])
        self.click_element(login['注销'])


if __name__ == "__main__":
    pass
