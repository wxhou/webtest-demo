#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from common.images import get_airtest_image
from airtest.core.cv import Template


def airtest_v(name):
    """被识别的图片"""
    return Template(name, record_pos=(12.32, 3.915), resolution=(1024, 768))


def airtest_touch_image(driver, name):
    """点击图片"""
    v = airtest_v(get_airtest_image(name))
    driver.airtest_touch(v)


def airtest_assert_template(driver, name, msg=None):
    """断言图片
    @param driver: 浏览器实例
    @param name: 图片的名称
    @param msg:
    """
    v = airtest_v(get_airtest_image(name))
    driver.assert_template(v, msg)
    return True


def airtest_assert_exists(driver, locator, msg=None):
    """断言文本在页面存在
    @param driver: 浏览器实例
    @param locator: 元素选择器(定位器)
    @param msg: 消息
    """
    operation, param = locator.split('==')  # 分类元素和方法
    driver.assert_exist(param, operation, msg)
    return True
