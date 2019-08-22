#!/usr/bin/env python3
# coding=utf-8
import unittest
from selenium import webdriver
from config.conf import driver_path
from Page.webpage import get_url, sleep
from PageObject.loginpage import Login
from utils.readconfig import ReadConfig
from utils.Imagecontrast import ImageCompare

conf = ReadConfig()
image = ImageCompare()


class TestLogin(unittest.TestCase):
    """登录功能"""

    @classmethod
    def setUpClass(cls) -> None:
        if conf.remote_state == 'True':
            cls.driver = webdriver.Remote(
                command_executor=conf.remote_server,
                desired_capabilities={'browserName': 'chrome'}
            )
        else:
            cls.driver = webdriver.Chrome(executable_path=driver_path)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        self.imgs = []
        get_url(conf.url, self.driver)

    def tearDown(self) -> None:
        pass

    def test_001(self):
        login = Login(self.driver)
        login.login('admin', '123456')
        sleep(3)
        login.quit_login()


if __name__ == '__main__':
    unittest.main(verbosity=2)
