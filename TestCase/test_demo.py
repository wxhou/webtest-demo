#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import unittest
from time import sleep
from airtest_selenium import WebChrome
from PageObject.loginpage import LoginPage
from common.readconfig import ini
from common.inspect_element import inspect_element
from common.airtest_method import airtest_assert_template, airtest_touch_image


class TestLogin(unittest.TestCase):
    """登录功能"""

    @classmethod
    def setUpClass(cls) -> None:
        inspect_element()
        cls.driver = WebChrome()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        self.imgs = []
        login = LoginPage(self.driver)
        login.get_url(ini.url)

    def tearDown(self):
        login = LoginPage(self.driver)
        login.quit_login()

    def test_001(self):
        login = LoginPage(self.driver)
        login.login('admin', '123456')
        sleep(3)
        airtest_touch_image(self.driver, 'CMS管理')
        sleep(3)
        airtest_assert_template(self.driver, '头像', "成功加载登录头像")


if __name__ == '__main__':
    unittest.main(verbosity=2)
