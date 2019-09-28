#!/usr/bin/env python3
# coding=utf-8
from Page.webpage import WebPage, sleep
from utils.readconfig import element
from config.conf import srceenshot_name




class Login(WebPage):
    def login(self, user, pwd):
        self.input_text(element('login', '账号'), text=user)
        self.input_text(element('login', '密码'), text=pwd)
        self.is_click(element('login', '登录'))
        sleep()

    def login_shot(self):
        self.screenshots_of_element(element('home', '头像'), screenshot_path=srceenshot_name)
        return srceenshot_name

    def quit_login(self):
        self.is_click(element('login', '用户头像'))
        self.is_click(element('login', '注销'))

if __name__ == "__main__":
    pass