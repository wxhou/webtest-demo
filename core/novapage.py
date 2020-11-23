#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException

from config.conf import element
from core.webpage import WebPage
from common.readelemnts import Element
from utils.logger import log
from utils.times import *
from utils.images import area_screenshot, get_image_name

base = Element(element['base'], 'base')


class NovaPage(WebPage):
    def assert_text_dom(self, text):
        """验证文字在DOM中"""
        assert self.is_exists(base['模糊匹配文字'] % text), f"文字{text}未在DOM中加载"

    def assert_text_visible(self, text):
        """验证文字是否可见"""
        assert self.is_visible(base['模糊匹配文字'] % text), f"文字{text}不可见"

    def element_screenshot(self, locator, path, number=None):
        """对某个元素进行截图,并返回截图路径"""
        ele = self.find_element(locator, number)
        self.focus(ele)  # 元素不可见则聚焦
        self.driver.save_screenshot(path)
        area_screenshot(ele, path)
        self.driver.implicitly_wait(1)
        log.info("截图的路径是：%s" % path)

    def upload_file(self, locator, path, number=None):
        """上传文件"""
        name = get_image_name(path)[0]
        ele = self.find_element(locator, number)
        self.focus(ele)
        ele.send_keys(path)
        log.info("正在上传文件：%s" % path)
        start_time = timestamp()
        while not self.is_exists("xpath==//*[contains(text(),'%s')]" % name):
            sleep(0.5)
            if (timestamp() - start_time) > self.timeout:
                raise TimeoutException("在元素【】上传文件【】失败" % ())
        log.info("上传文件【%s】成功！" % path)
