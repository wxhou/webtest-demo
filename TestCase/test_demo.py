#!/usr/bin/env python3
# coding=utf-8
import unittest
from selenium import webdriver
from utils.readconfig import ReadConfig
from config.conf import driver_path
from Page.webpage import sleep
from PageObject.loginpage import Login
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
        self.login = Login(self.driver)
        self.login.get_url(conf.url)

    def tearDown(self) -> None:
        pass

    def test_001(self):
        self.login.login('admin', '123456')
        sleep(3)
        self.login.quit_login()


if __name__ == '__main__':
    unittest.main(verbosity=2)
