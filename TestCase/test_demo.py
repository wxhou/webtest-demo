#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   test_demo.py
@Time    :   2019/09/28 11:12:03
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys
sys.path.append('.')
import unittest
from selenium import webdriver
from settings import driver_path
from Page.webpage import WebPage,sleep
from PageObject.loginpage import Login
from common.Imagecontrast import ic
from common.readconfig import ini
from utils.data_generator import gen


class TestLogin(unittest.TestCase):
    """登录功能"""
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=driver_path)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        self.imgs = []
        login = Login(self.driver)
        login.get_url(ini.url)

    def tearDown(self):
        login = Login(self.driver)
        login.quit_login()

    def test_001(self):
        login = Login(self.driver)
        login.login('admin', '123456')
        sleep(3)
        head = login.login_shot(gen.screenshot_name)
        self.driver.refresh()
        assert ic(
            head,
            gen.screen_expected) == 0.0, "当前元素截图%s，与预期图片%s不匹配" % (head,
                                                              gen.screen_expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
