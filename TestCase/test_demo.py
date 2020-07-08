#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import unittest
from airtest_selenium import WebChrome
from page_object.loginpage import LoginPage
from common.inspect_element import inspect_element
from basic.airtest_method import AirTestMethod
from common.readconfig import ini

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
        cls.login.get_url(ini.url)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.login.quit_login()

    def setUp(self) -> None:
        self.imgs = []

    def test_001(self):
        self.login.login('admin', 'Hoou1993')
        self.airtest.assert_template('项目头像', "成功加载登录头像")


if __name__ == '__main__':
    unittest.main(verbosity=2)
