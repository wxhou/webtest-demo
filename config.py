#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from common.readconfig import ReadConfig
from selenium.webdriver.common.by import By

# 项目的根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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

# 测试应用管理
apps = {
    'zentao': os.path.join(BASE_DIR, 'apps', 'zentao')
}

# 测试配置文件管理
ini = {
    'zentao': ReadConfig(apps['zentao'])
}

# 测试元素管理
element = {
    'base': os.path.join(BASE_DIR, 'apps'),
    'zentao': os.path.join(apps['zentao'], 'page', 'elements')
}

# 测试图片管理
airimages = {
    'zentao': os.path.join(apps['zentao'], 'page', 'images')
}

# 测试集
tests = {
    'zentao': os.path.join(apps['zentao'], 'tests')
}

if __name__ == "__main__":
    print(BASE_DIR)
    print(ini['zentao'].url)
