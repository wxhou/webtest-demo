#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from common.images import get_airtest_image
from airtest.core.cv import Template


class AirTestMethod:
    """airtest-selenium方法"""

    def __init__(self, driver):
        self.driver = driver
        self._size = self.driver.get_window_size()

    @property
    def size(self):
        return self._size['width'], self._size['height']

    @property
    def size_half(self):
        return self._size['width'] / 2, self._size['height'] / 2

    def _image(self, name):
        """被识别的图片Template对象"""
        return Template(name, record_pos=self.size_half, resolution=self.size)

    def touch_image(self, name):
        """点击网页中的图片
        @param driver: 浏览器实例
        @param name: 图片名称
        """
        v = self._image(get_airtest_image(name))
        self.driver.airtest_touch(v)

    def assert_template(self, name, msg=None):
        """验证网页中图片存在
        @param driver: 浏览器实例
        @param name: 图片的名称
        @param msg:
        """
        v = self._image(get_airtest_image(name))
        self.driver.assert_template(v, msg)


if __name__ == '__main__':
    pass
