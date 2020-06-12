#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import unittest
from airtest_selenium import WebChrome
from page_object.loginpage import LoginPage
from tools.clear_data import clear_old_data
from common.inspect_element import inspect_element
from common.airtest_method import AirTestMethod
from common.readconfig import ini
from config.conf import TEST_SUITES

driver = None


def setUpModule():
    global driver
    if driver is None:
        inspect_element()
        driver = WebChrome()


def tearDownModule():
    driver.quit()


class TestLogin(unittest.TestCase):
    """登录功能"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.airtest = AirTestMethod(driver)
        cls.login = LoginPage(driver)

    @classmethod
    def tearDownClass(cls) -> None:
        clear_old_data(TEST_SUITES)

    def setUp(self) -> None:
        self.imgs = []
        self.login.get_url(ini.url)

    def tearDown(self):
        self.login.quit_login()

    def test_001(self):
        self.login.login('admin', '123456')
        self.airtest.touch_image('CMS管理')
        self.airtest.assert_template('头像', "成功加载登录头像")


if __name__ == '__main__':
    unittest.main(verbosity=2)
