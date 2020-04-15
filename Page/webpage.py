#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from utils.images import element_screenshot, get_image_name
from common.readelemnts import Element
from utils.logger import log
from utils.times import sleep
import time
import conf

"""
selenium基类
本文件存放了selenium基类的深度封装方法
"""
base = Element('base')


class WebPage:
    """selenium基类"""

    def __init__(self, driver):
        # self.driver = WebChrome()
        self.driver = driver
        self.timeout = 10
        self.visible = 3
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.action = ActionChains(self.driver)
        self.touch = TouchActions(self.driver)

    @staticmethod
    def element_value(locator, number):
        """元素值"""
        return locator % number if number else locator

    @staticmethod
    def selector(func, locator, number=None):
        """选择器"""
        pattern, value = locator.split('==')
        return func(conf.LOCATE_MODE[pattern], WebPage.element_value(value, number))

    def get_url(self, url, title=None):
        """打开网址并验证"""
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("\t打开网页：%s" % url)
        except TimeoutException:
            raise ("打开%s超时,请检查网络或网址服务器" % url)
        if title:
            title2 = self.driver.title
            assert EC.title_is(title)(self.driver), "网页title不正确，应为%s，实为%s" % (title, title2)

    def find_web_element(self, locator, number=None):
        """寻找单个元素"""
        return WebPage.selector(
            lambda *args: self.wait.until(lambda x: x.find_element(*args),
                                          message="查找单个元素%s失败！" % WebPage.element_value(locator, number)),
            locator, number)

    def find_web_elements(self, locator, number=None):
        """查找多个相同的元素"""
        return WebPage.selector(
            lambda *args: self.wait.until(lambda x: x.find_elements(*args),
                                          message="查找单个元素%s失败！" % WebPage.element_value(locator, number)),
            locator, number)

    """获取函数"""

    def element_num(self, locator):  # 获取相同元素的个数
        """获取相同元素的个数"""
        number = len(self.find_web_elements(locator))
        log.info("元素%s数量是：%s" % (locator, number))
        return number

    def element_text(self, locator, number=None):
        """获取当前的text"""
        text = self.find_web_element(locator, number).text
        log.info("元素%s文字是：[%s]" % (WebPage.element_value(locator, number), text))
        return text

    """判断函数"""

    def element_exists(self, locator, number=None):  # 判断元素是否在DOM中
        """元素是否存在(DOM)"""
        try:
            WebPage.selector(lambda *args: EC.presence_of_element_located(args)(self.driver),
                             locator, number=number)
            return True
        except:
            return False

    def element_visible(self, locator, number=None):
        """元素是否可见"""
        try:
            WebPage.selector(lambda *args: WebDriverWait(self.driver, self.visible).until(
                EC.visibility_of_element_located(args)), locator, number)
            return True
        except:
            return False

    def page_refresh(self, locator, number=None):
        """判断页面是否刷新"""
        ele = self.find_web_element(locator, number)
        return EC.staleness_of(ele)

    def text_in_element(self, locator, text, number=None):
        """检查某段文本是否在元素中"""
        log.info("检查文本【%s】在输入框%s中" % (text, WebPage.element_value(locator, number)))
        return WebPage.selector(lambda *args: EC.text_to_be_present_in_element(args, text)(
            self.driver), locator, number)

    def is_selected(self, locator, number=None):
        """判断是否选中"""
        log.info("检查元素:%s 是否被选中" % WebPage.element_value(locator, number))
        return WebPage.selector(lambda *args: self.wait.until(
            EC.element_located_selection_state_to_be(args, True)), locator, number)

    def alert_text_exists(self):
        """判断弹框是否出现，并返回弹框的文字"""
        alert = EC.alert_is_present()(self.driver)
        text = alert.text
        log.info("Alert弹窗提示为：%s" % text)
        alert.accept()
        return text

    """操作函数"""

    def focus(self, element):  # 该函数的编写来源于robot-framework-selenium
        """聚焦元素"""
        self.driver.execute_script("arguments[0].focus();", element)

    def clear_input_box(self, locator, number=None):
        """清空输入框"""
        ele = self.find_web_element(locator, number)
        self.focus(ele)
        ele.clear()
        log.info("清空输入框：%s" % WebPage.element_value(locator, number))
        self.driver.implicitly_wait(1)

    def input_text(self, locator, text, number=None):
        """输入(输入前先清空)"""
        sleep(0.5)
        msg = WebPage.element_value(locator, number)
        ele = WebPage.selector(lambda *args: self.wait.until(
            EC.element_to_be_clickable(args), message="在元素%s中，输入【%s】失败！" % (msg, text)), locator, number)
        self.focus(ele)
        ele.clear()
        ele.send_keys(text)
        log.info("在元素%s中输入%s" % (WebPage.element_value(locator, number), text))

    def click_element(self, locator, number=None):
        """点击"""
        msg = WebPage.element_value(locator, number)
        ele = WebPage.selector(lambda *args: self.wait.until(
            EC.element_to_be_clickable(args), message="点击元素%s失败！" % msg), locator, number)
        self.focus(ele)
        ele.click()
        log.info("点击元素%s" % msg)
        sleep()

    def action_click(self, locator, number=None):
        """使用鼠标点击"""
        element = self.find_web_element(locator, number)
        self.focus(element)
        self.action.pause(0.5).click(element).pause(0.5).perform()
        log.info("使用鼠标点击：%s" % WebPage.element_value(locator, number))
        self.driver.implicitly_wait(1)

    def action_input(self, locator, text, number=None):
        """action的输入方法"""
        element = self.find_web_element(locator, number)
        self.focus(element)
        self.action.pause(0.5).click(element).pause(0.5).send_keys(text)
        self.action.perform()
        log.info("使用鼠标方法输入：%s" % text)
        self.action.actions.pop()  # 防止重复输入

    def inline_scroll_bar(self, element, func='Left', number='10000'):
        """
        内嵌滚动条（默认为向右滚动）
        :param func: ['Left','Top']
        :param number: ['10000','0']
        """
        js1 = 'document.getElementsByClassName("%s")[0].scroll%s=%s' % (element, func, number)
        self.driver.execute_script(js1)

    def upload_file(self, locator, path, number=None):
        """上传文件"""
        name = get_image_name(path)[0]
        ele = self.find_web_element(locator, number)
        self.focus(ele)
        ele.send_keys(path)
        log.info("正在上传文件：%s" % path)
        start_time = time.time()
        while not self.element_exists(base['模糊匹配文字'] % name):
            sleep(0.5)
            if (time.time() - start_time) > self.timeout:
                raise TimeoutException("在元素【】上传文件【】失败" % ())
        log.info("上传文件【%s】成功！" % path)

    def element_screenshots(self, locator, path, number=None):
        """对某个元素进行截图,并返回截图路径"""
        ele = self.find_web_element(locator, number)
        self.focus(ele)  # 元素不可见则聚焦
        self.driver.save_screenshot(path)
        element_screenshot(ele, path)
        self.driver.implicitly_wait(1)
        log.info("截图的路径是：%s" % path)
        return path

    def select_drop_down(self, locator, number=None):
        """选择下拉框"""
        ele = self.find_web_element(locator, number)
        self.focus(ele)
        sleep(2)
        # 这里一定要加等待时间，否则会引起如下报错
        # Element is not currently visible and may not be manipulated
        return Select(ele)

    def switch_to_frame(self, locator, number=None):
        """切换iframe"""
        log.info("切换最新的iframe")
        return WebPage.selector(lambda *args: self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(args)), locator, number)

    def switch_windows_handle(self):
        """切换最新的标签"""
        now_handle1 = self.driver.current_window_handle
        all_handle = self.driver.window_handles
        self.driver.switch_to.window(all_handle[-1])
        now_handle2 = self.driver.current_window_handle
        assert now_handle1 != now_handle2, "切换标签失败!"

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        log.info("刷新当前网页!")
        self.driver.implicitly_wait(30)


if __name__ == "__main__":
    pass
