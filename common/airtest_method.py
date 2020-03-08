#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from common.images import get_airtest_image
from airtest.core.cv import Template


def airtest_image(name):
    """被识别的图片Template对象"""
    return Template(name, record_pos=(12.32, 3.915), resolution=(1200, 768))


def airtest_touch_image(driver, name):
    """点击网页中的图片
    @param driver: 浏览器实例
    @param name: 图片名称
    """
    v = airtest_image(get_airtest_image(name))
    driver.airtest_touch(v)


def airtest_assert_template(driver, name, msg=None):
    """验证网页中图片存在
    @param driver: 浏览器实例
    @param name: 图片的名称
    @param msg:
    """
    v = airtest_image(get_airtest_image(name))
    driver.assert_template(v, msg)
