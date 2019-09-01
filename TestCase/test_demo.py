#!/usr/bin/env python3
# coding=utf-8
import unittest
from selenium import webdriver
from config.conf import driver_path
from Page.webpage import get_url, sleep
from PageObject.loginpage import Login
from utils.readconfig import ReadConfig
from utils.Imagecontrast import ImageContrast
from utils.data_generator import Generator

conf = ReadConfig()
gen = Generator()
ic = ImageContrast()


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

    def test_001(self):
        login = Login(self.driver)
        login.login('admin', '123456')
        sleep(3)
        head = login.login_shot()
        assert ic(head, gen.screen_name) == 0.0
        login.quit_login()


if __name__ == '__main__':
    unittest.main(verbosity=2)
