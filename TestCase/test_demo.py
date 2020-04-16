#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import conf
import unittest
from utils.times import sleep
from utils.clear_data import clear_old_data
from airtest_selenium import WebChrome
from PageObject.loginpage import LoginPage
from common.inspect_element import inspect_element
from common.airtest_method import AirTestMethod


class TestLogin(unittest.TestCase):
    """登录功能"""

    @classmethod
    def setUpClass(cls) -> None:
        inspect_element()
        cls.driver = WebChrome()
        cls.airtest = AirTestMethod(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        clear_old_data(conf.TEST_SUITES)

    def setUp(self) -> None:
        self.imgs = []
        login = LoginPage(self.driver)
        login.get_url(conf.HOST)

    def tearDown(self):
        login = LoginPage(self.driver)
        login.quit_login()

    def test_001(self):
        login = LoginPage(self.driver)
        login.login('admin', '123456')
        sleep(3)
        self.airtest.touch_image('CMS管理')
        sleep(3)
        self.airtest.assert_template('头像', "成功加载登录头像")


if __name__ == '__main__':
    unittest.main(verbosity=2)
