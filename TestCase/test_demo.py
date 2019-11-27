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
from PageObject.loginpage import Login
from common.image import picture
from common.readconfig import ini
from utils.produce import produce
from utils.dirty_data import dirty_data
from time import sleep


class TestLogin(unittest.TestCase):
    """登录功能"""
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        dirty_data()

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
        new_picture = login.login_shot(produce.screenshot_name)
        self.driver.refresh()
        assert picture(new_picture,
                       produce.screen_expected) == 0.0, "当前元素截图%s，与预期图片%s不匹配" % (
                           new_picture, produce.screen_expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
