#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import unittest
from config.conf import ini, airimages
from airtest_selenium import WebChrome
from core.aircore import AirTestMethod
from common.readimage import get_image
from apps.zentao.page.objects.loginpage import LoginPage

driver = None


def setUpModule():
    global driver
    if driver is None:
        driver = WebChrome()


def tearDownModule():
    driver.quit()


class TestLogin(unittest.TestCase):
    """登录功能"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.airtest = AirTestMethod(driver)
        cls.login = LoginPage(driver)
        cls.login.get_url(ini['zentao'].url)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.login.quit_login()

    def setUp(self) -> None:
        self.imgs = []

    def test_001(self):
        self.login.login('admin', 'Hoou1993')
        self.airtest.assert_template(get_image(airimages['zentao'], '项目头像'), "成功加载登录头像")


if __name__ == '__main__':
    unittest.main(verbosity=2)
