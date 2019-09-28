#!/usr/bin/env python3
# coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium import webdriver
from PIL import Image
import time


def sleep(seconds=1):
    '''
    等待时间
    :return 有些提示框不强制等待，只用显式等待会导致执行报错
    '''
    time.sleep(seconds)


def get_url(url, driver):
    '''打开网址并验证'''
    driver.set_page_load_timeout(60)
    try:
        driver.maximize_window()
        driver.get(url)
    except TimeoutException:
        raise ("打开%s超时请检查网络或网址服务器" % url)
    assert EC.url_to_be(url)(driver), "地址不正确，应为%s，实为%s" % (url,
                                                           driver.current_url)


class WebPage:
    """selenium基类"""
    def __init__(self, driver):
        self.locate_mode = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'name': By.NAME,
            'id': By.ID
        }  # 元素定位的类型

        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.action = ActionChains(self.driver)
        self.touch = TouchActions(self.driver)

    def function(self, func, locator, number=None):
        """共用方法"""
        pattern, value = locator.split('==')
        if pattern in self.locate_mode:
            try:
                if number:
                    element = func(self.locate_mode[pattern], value % number)
                else:
                    element = func(self.locate_mode[pattern], value)
            except InvalidElementStateException:
                print("元素%s，清除输入框内容失败，用户不可编辑" % locator)
                return
            except NoSuchElementException:
                print('当前页面没有找到元素%s' % locator)
                return
            except TimeoutException:
                print('查找元素%s超时' % locator)
                return
            except Exception as e:
                raise e
            else:
                return element
        else:
            raise ('element type is not "CSS"')

    def get_url(self, url):
        '''打开网址并验证'''
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
        except TimeoutException:
            raise ("打开%s超时请检查网络或网址服务器" % url)
        assert EC.url_contains(url)(
            self.driver), "地址包含关系不正确，应为%s，实为%s" % (url,
                                                   self.driver.current_url)

    def Assert_title(self, text):
        title1 = EC.title_is(text)
        title2 = self.driver.title
        assert title1(self.driver), "title不正确，应为%s，实为%s" % (text, title2)

    def findelement(self, locator, number=None):
        """寻找单个元素"""
        function = lambda *args: self.wait.until(lambda x: x.find_element(*args
                                                                          ))
        return self.function(function, locator, number)

    def findelements(self, locator, number=None):
        '''查找多个相同的元素'''
        function = lambda *args: self.wait.until(lambda x: x.find_elements(
            *args))
        return self.function(function, locator, number)

    def is_clear(self, locator, number=None):
        '''清空输入框'''
        self.findelement(locator, number).clear()
        self.driver.implicitly_wait(0.5)

    def input_text(self, locator, number=None, text=None):
        '''输入(输入前先清空)'''
        self.is_clear(locator, number)
        self.findelement(locator, number).send_keys(text)

    def is_click(self, locator, number=None):
        '''点击'''
        function = lambda *args: self.wait.until(
            EC.element_to_be_clickable(args))
        ele = self.function(function, locator, number)
        ele.click()
        sleep()

    def isElementText(self, locator, number=None):
        '''获取当前的text'''
        return self.findelement(locator, number).text

    def textInElement(self, locator, number=None, text=None):
        '''检查某段文本在输入框中'''
        function = lambda *args: EC.text_to_be_present_in_element(args, text)(
            self.driver)
        return self.function(function, locator, number)

    def isElementNum(self, locator):
        '''获取相同元素的个数'''
        return len(self.findelements(locator))

    def isElementExists(self, locator, number=None):
        '''元素是否可见'''
        function = lambda *args: self.wait.until(
            EC.visibility_of_element_located(args))
        if self.function(function, locator, number):
            return True
        else:
            return False

    def isSelected(self, locator, number=None):
        '''判断是否选中'''
        function = lambda *args: EC.element_located_selection_state_to_be(
            args, True)(self.driver)
        return self.function(function, locator, number)

    def action_click(self, locator, number=None):
        '''使用鼠标点击'''
        sleep()
        element = self.findelement(locator, number)
        self.driver.implicitly_wait(1)
        self.action.click(element).perform()
        sleep()

    def action_sendkeys(self, locator, number=None, text=None):
        '''action的输入方法'''
        sleep()
        element = self.findelement(locator, number)
        sleep()
        self.is_click(locator, number)
        self.action.click(element).send_keys(text)
        self.action.perform()
        self.action._actions.pop()  # 防止重复输入

    def upload_File(self, locator, number=None, filepath=None):
        '''上传文件'''
        self.findelement(locator, number).send_keys(filepath)
        sleep(5)

    def alertTextExists(self):
        "判断弹框是否出现，并返回弹框的文字"
        try:
            alert = EC.alert_is_present()(self.driver)
            text = alert.text
        except Exception as e:
            raise e
        else:
            alert.accept()
            return text

    def switchToFrame(self, locator, number=None):
        """切换iframe"""
        function = lambda *args: self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(args))
        return self.function(function, locator, number)

    def switchToDefaultFrame(self):
        """返回默认"""
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print(format(e))

    def switchWindowshandle(self):
        '''切换最新的标签'''
        now_handle1 = self.driver.current_window_handle
        all_handle = self.driver.window_handles
        self.driver.switch_to.window(all_handle[-1])
        now_handle2 = self.driver.current_window_handle
        for i in range(3, 0, -1):
            try:
                assert now_handle1 != now_handle2
                print('切换新标签成功！%s' % self.driver.title)
                break
            except AssertionError:
                print("切换标签失败！正在重试，还有%d机会！" % i)
        else:
            print("切换标签失败!请检查！")

    def screenshots_of_element(self,
                               locator,
                               number=None,
                               screenshot_path=None):
        '''对某个元素进行截图,并返回截图路径'''
        ele = self.findelement(locator, number)
        self.driver.save_screenshot(screenshot_path)
        self.shot_file(screenshot_path)
        print("需要截图的元素坐标%s" % ele.location)
        print("需要截图的元素大小%s" % ele.size)
        shot = (ele.location['x'], ele.location['y'],
                ele.location['x'] + ele.size['width'],
                ele.location['y'] + ele.size['height'])
        im = Image.open(screenshot_path)
        im = im.crop(shot)
        im.save(screenshot_path)
        sleep()
        return screenshot_path

    def focus(self, locator, number=None):
        # 该函数的编写来源于robot-framework-selenium
        """聚焦元素"""
        sleep()
        ele = self.findelement(locator, number)
        self.driver.execute_script("arguments[0].focus();", ele)

    def click_drop_down(
            self,
            selectlocator,
            selectnumber=None,
            optionlocator=None,
            optionnumber=None,
    ):
        """封装两次点击"""
        self.is_click(selectlocator, selectnumber)
        self.is_click(optionlocator, optionnumber)

    def select_drop_down(self,
                         locator,
                         number=None,
                         index=None,
                         value=None,
                         text=None):
        """选择下拉框"""
        ele = self.findelement(locator, number)
        sleep(2)
        # 这里一定要加等待时间，否则会引起如下报错
        # Element is not currently visible and may not be manipulated
        if value:
            Select(ele).select_by_index(index)
        elif index:
            Select(ele).select_by_value(value)
        elif text:
            Select(ele).select_by_visible_text(text)

    def getSource(self):
        """获取页面源代码"""
        return self.driver.page_source

    def shot_file(self, path):
        '''文件截图截图'''
        return self.driver.save_screenshot(path)

    def close(self):
        '''关闭当前标签'''
        self.driver.close()

    def refresh(self):
        '''刷新页面F5'''
        self.driver.refresh()
        self.driver.implicitly_wait(30)


if __name__ == '__main__':
    pass
