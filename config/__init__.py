#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from selenium.webdriver.common.by import By

# 项目的根目录
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# 日志目录
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 报告目录
REPORT_DIR = os.path.join(BASE_DIR, 'report')

# 截图目录
SCREEN_DIR = os.path.join(BASE_DIR, 'screen_capture')

# 元素定位的类型
LOCATE_MODE = {
    'css': By.CSS_SELECTOR,
    'xpath': By.XPATH,
    'name': By.NAME,
    'id': By.ID,
    'class': By.CLASS_NAME
}

if __name__ == '__main__':
    print(BASE_DIR)
