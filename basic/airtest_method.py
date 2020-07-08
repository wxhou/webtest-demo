#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from tools.images import get_airtest_image
from config.conf import SCREEN_DIR
from airtest.core.settings import Settings as ST
from airtest.core.cv import Template
from basic.webpage import WebPage
from tools.times import sleep

# 设置airtest产生的截图目录
ST.LOG_DIR = SCREEN_DIR


class AirTestMethod(WebPage):
    """airtest-selenium方法"""

    # 此类在Windows平台下无法使用，只能在MacOS平台下使用
    def __init__(self, driver):
        super().__init__(driver)
        self._size = self.driver.get_window_size()

    @property
    def size(self):
        return self._size['width'], self._size['height']

    @property
    def size_half(self):
        return self._size['width'] / 2, self._size['height'] / 2

    def template(self, name):
        """被识别的图片Template对象"""
        return Template(name, record_pos=self.size_half, resolution=self.size)

    def touch_image(self, name):
        """点击网页中的图片
        @param name: 图片名称
        """
        v = self.template(get_airtest_image(name))
        self.driver.airtest_touch(v)
        sleep(3)

    def assert_template(self, name, msg=None):
        """验证网页中图片存在
        @param name: 图片的名称
        @param msg:
        """
        v = self.template(get_airtest_image(name))
        self.driver.assert_template(v, msg)


if __name__ == '__main__':
    pass
