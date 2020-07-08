#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import os
import platform
from selenium.webdriver.common.by import By

# 项目的根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件目录
INI_DIR = os.path.join(BASE_DIR, 'config', 'config.ini')

# 页面元素的目录
ELEMENT_DIR = os.path.join(BASE_DIR, 'page_element')

# airtest目录
PAGE_IMAGES = os.path.join(BASE_DIR, 'page_images')

# 日志目录
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 报告目录
REPORT_DIR = os.path.join(BASE_DIR, 'report')

# 截图目录
SCREEN_DIR = os.path.join(BASE_DIR, 'screen_capture')

# 测试集
TEST_DIR = os.path.join(BASE_DIR, 'TestCase')

# 系统信息
SYS_INFO = platform.platform()

# 元素定位的类型
LOCATE_MODE = {
    'css': By.CSS_SELECTOR,
    'xpath': By.XPATH,
    'name': By.NAME,
    'id': By.ID,
    'class': By.CLASS_NAME
}

if __name__ == "__main__":
    print(BASE_DIR)
    print(SYS_INFO)
