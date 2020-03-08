#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from Page.webpage import WebPage, sleep
from common.readelemnts import Element

login = Element('login')
home = Element('home')


class LoginPage(WebPage):
    def login(self, user, pwd):
        self.input_text(login('账号'), text=user)
        self.input_text(login('密码'), text=pwd)
        self.is_click(login('登录'))
        sleep()

    def quit_login(self):
        self.is_click(login('用户头像'))
        self.is_click(login('注销'))


if __name__ == "__main__":
    pass
