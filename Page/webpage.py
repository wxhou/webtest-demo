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
    assert EC.url_to_be(url)(driver), "地址不正确，应为%s，实为%s" % (url, driver.current_url)


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

    def Assert_title(self, text):
        title = EC.title_is(text)
        _title1 = self.driver.title
        assert title(self.driver), "title不正确，应为%s，实为%s" % (text, _title1)

    def findElement(self, element, number=None):
        '''寻找单个元素'''
        pattern, value = element.split('>')
        if pattern in self.locate_mode:
            try:
                if number:
                    ele = self.wait.until(
                        EC.presence_of_element_located((self.locate_mode[pattern], value % number)))
                else:
                    ele = self.wait.until(
                        EC.presence_of_element_located((self.locate_mode[pattern], value)))

            except NoSuchElementException:
                raise ('当前页面没有找到元素%s' % value)
            except TimeoutException:
                raise ('查找元素%s超时' % value)
            except Exception as e:
                raise e
            else:
                return ele
        else:
            raise ('element type is not "CSS"')

    def findElements(self, element, number=None):
        '''查找多个相同的元素'''
        pattern, value = element.split('>')
        if pattern in self.locate_mode:
            try:

                if number:
                    eles = self.wait.until(
                        EC.presence_of_all_elements_located((self.locate_mode[pattern], value % number)))
                else:
                    eles = self.wait.until(
                        EC.presence_of_all_elements_located((self.locate_mode[pattern], value)))

            except NoSuchElementException:
                raise ('当前页面没有找到元素%s' % value)
            except TimeoutException:
                raise ('查找元素%s超时' % value)
            except Exception as e:
                raise e
            else:
                return eles
        else:
            raise ('element type is not "CSS"')

    def input_text(self, locator, text):
        '''输入(输入前先清空)'''
        self.is_clear(locator)
        self.driver.implicitly_wait(0.5)
        if isinstance(locator, tuple):
            self.findElement(*locator).send_keys(text)
        else:
            self.findElement(locator).send_keys(text)

    def focus(self, locator, number=None):
        # 该函数的编写来源于robot-framework-selenium
        """聚焦元素"""
        sleep()
        pattern, value = locator.split('>')
        if pattern in self.locate_mode:
            if number:
                element = self.driver.find_element(self.locate_mode[pattern], value % number)
            else:
                element = self.driver.find_element(self.locate_mode[pattern], value)
            self.driver.execute_script("arguments[0].focus();", element)

    def is_clear(self, locator):
        '''清空输入框'''
        try:
            if isinstance(locator, tuple):
                self.findElement(*locator).clear()
            else:
                self.findElement(locator).clear()
        except InvalidElementStateException:
            print("元素%s，清除输入框内容失败，用户不可编辑" % locator)

    def is_click(self, element, number=None):
        '''点击'''
        pattern, value = element.split('>')
        if pattern in self.locate_mode:
            try:
                if number:
                    ele = self.wait.until(
                        EC.element_to_be_clickable((self.locate_mode[pattern], value % number)))
                else:
                    ele = self.wait.until(
                        EC.element_to_be_clickable((self.locate_mode[pattern], value)))
            except NoSuchElementException:
                raise ('当前页面没有找到元素%s' % value)
            except TimeoutException:
                raise ('查找元素%s超时' % value)
            except Exception as e:
                raise e
            else:
                ele.click()
                sleep()
        else:
            raise ('element type is not "CSS"')

    def isElementText(self, locator):
        '''获取当前的text'''
        if isinstance(locator, tuple):
            _text = self.findElement(*locator).text
        else:
            _text = self.findElement(locator).text
        return _text

    def textInElement(self, element, number=None, text=None):
        '''检查某段文本在输入框中'''
        pattern, value = element.split('>')
        if pattern in self.locate_mode:
            try:
                if number:
                    eletxt = EC.text_to_be_present_in_element((self.locate_mode[pattern], value % number), text)(
                        self.driver)
                else:
                    eletxt = EC.text_to_be_present_in_element((self.locate_mode[pattern], value), text)(self.driver)
            except Exception as e:
                raise e
            else:
                return eletxt
        else:
            raise ('Element type is not "CSS"')

    def isElementNum(self, locator):
        '''获取相同元素的个数'''
        if isinstance(locator, tuple):
            _num = self.findElements(*locator)
        else:
            _num = self.findElements(locator)
        return len(_num)

    def isElementExists(self, element, number=None):
        '''元素是否可见,等待3S'''
        wait = WebDriverWait(self.driver, 3)
        pattern, value = element.split('>')
        if pattern in self.locate_mode:
            try:
                if number:
                    wait.until(
                        EC.visibility_of_element_located((self.locate_mode[pattern], value % number)))
                else:
                    wait.until(
                        EC.visibility_of_element_located((self.locate_mode[pattern], value)))
            except (NoSuchElementException, TimeoutException):
                return False
            except StaleElementReferenceException:
                print("当前元素不在当前的页面中，当前页面%s，元素%s" % (self.driver.current_url, value))
                return False
            except Exception as e:
                raise e
            else:
                return True
        else:
            raise ('element type is not "css"')

    def isSelected(self, element, number=None):
        '''判断是否选中'''
        pattern, value = element.split('>')
        if pattern in self.locate_mode:
            try:
                if number:
                    Exists = EC.element_located_selection_state_to_be((self.locate_mode[pattern], value % number),
                                                                      True)(
                        self.driver)
                else:
                    Exists = EC.element_located_selection_state_to_be((self.locate_mode[pattern], value), True)(
                        self.driver)
            except Exception as e:
                raise e
            else:
                return Exists
        else:
            raise ('element type is not "css"')

    def action_click(self, locator):
        '''使用鼠标点击'''
        sleep()
        if isinstance(locator, tuple):
            _element = self.findElement(*locator)
        else:
            _element = self.findElement(locator)
        self.driver.implicitly_wait(1)
        self.action.click(_element).perform()
        sleep()

    def action_sendkeys(self, locator, text):
        '''action的输入方法'''
        sleep()
        if isinstance(locator, tuple):
            _element = self.findElement(*locator)
            self.is_click(*locator)
        else:
            _element = self.findElement(locator)
            self.is_click(locator)
        self.driver.implicitly_wait(1)
        self.action.click(_element).send_keys(text).perform()

    def upload_File(self, element, number=None, filepath=None):
        '''上传文件'''
        pattern, value = element.split('>')
        if pattern in self.locate_mode:
            try:
                if number:
                    ele = self.driver.find_element(self.locate_mode[pattern], value % number)
                else:
                    ele = self.driver.find_element(self.locate_mode[pattern], value)
            except NoSuchElementException:
                raise ('当前页面没有找到元素%s' % value)
            except TimeoutException:
                raise ('查找元素%s超时' % value)
            except Exception as e:
                raise e
            else:
                if not filepath:
                    raise ("upload_File方法没有指定上传的文件")
                sleep()
                ele.send_keys(filepath)
                sleep()
        else:
            raise ('element type is not "CSS"')

    def alertTextExists(self):
        "判断弹框是否出现"
        try:
            alert = EC.alert_is_present()(self.driver)
            text = alert.text
        except Exception as e:
            raise e
        else:
            alert.accept()
            return text

    def switchToFrame(self, element, number=None):
        """切换iframe"""
        pattern, value = element.split('>')
        if pattern in self.locate_mode:
            try:
                if number:
                    frame = self.wait.until(
                        EC.frame_to_be_available_and_switch_to_it((self.locate_mode[pattern], value % number)))
                else:
                    frame = self.wait.until(
                        EC.frame_to_be_available_and_switch_to_it((self.locate_mode[pattern], value % number)))
            except NoSuchElementException:
                raise ('当前页面没有找到元素%s' % value)
            except TimeoutException:
                raise ('查找元素%s超时' % value)
            except Exception as e:
                raise e
            else:
                return frame

    def switchToDefaultFrame(self):
        """返回默认"""
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print(format(e))

    def screenshots_of_element(self, element, number=None, screenshot_path=None):
        '''对某个元素进行截图,并返回截图路径'''
        pattern, value = element.split('>')
        if pattern in self.locate_mode:
            try:
                if number:
                    ele = self.wait.until(
                        EC.visibility_of_element_located((self.locate_mode[pattern], value % number)))
                else:
                    ele = self.wait.until(
                        EC.visibility_of_element_located((self.locate_mode[pattern], value)))
            except (NoSuchElementException, TimeoutException):
                raise ("当前元素找不到，或查找超时！", format(value))
            except StaleElementReferenceException:
                raise ("当前元素不在当前的页面中，当前页面%s，元素%s" % (self.driver.current_url, value))
            except Exception as e:
                raise e
            else:
                self.shot(screenshot_path)
                print("需要截图的元素坐标%s" % ele.location)
                print("需要截图的元素大小%s" % ele.size)
                shot = (ele.location['x'],
                        ele.location['y'],
                        ele.location['x'] + ele.size['width'],
                        ele.location['y'] + ele.size['height'])
                im = Image.open(screenshot_path)
                im = im.crop(shot)
                im.save(screenshot_path)
                sleep()
        else:
            raise ('element type is not "css"')

    def getSource(self):
        """获取页面源代码"""
        return self.driver.page_source

    def shot(self, path):
        '''base64截图'''
        return self.driver.save_screenshot(path)

    def roll(self, locator):
        '''执行Windows脚本'''
        self.driver.execute_script(locator)

    def close(self):
        '''关闭当前标签'''
        self.driver.close()

    def refresh(self):
        '''刷新页面F5'''
        self.driver.refresh()
        self.driver.implicitly_wait(30)


if __name__ == '__main__':
    pass
