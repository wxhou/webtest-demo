#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import os
import platform
from selenium.webdriver.common.by import By

# 项目的根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 配置文件目录
INI_PATH = os.path.join(BASE_DIR, 'config.ini')

# 页面元素的目录
ELEMENT_PATH = os.path.join(BASE_DIR, 'PageElements')

# airtest目录
AIRTEST_PATH = os.path.join(BASE_DIR, 'airtest_image')

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'logs')

# 报告目录
REPORT_PATH = os.path.join(BASE_DIR, 'report')

# 测试集
TEST_SUITES = os.path.join(BASE_DIR, 'TestCase')

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
