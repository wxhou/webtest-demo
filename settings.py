#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   settings.py
@Time    :   2019/11/18 14:16:26
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys
sys.path.append('.')
import os
import platform

#项目的根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#配置文件目录
INI_PATH = os.path.join(BASE_DIR, 'config.ini')

#页面元素的目录
ELEMENT_PATH = lambda x: os.path.join(BASE_DIR, 'PageElements', '%s.yaml' % x)

# 截图目录
SCREENSHOT_PATH = os.path.join(BASE_DIR, 'screenshot')

# 数据库目录
DB_PATH = os.path.join(BASE_DIR, 'TestData', 'sqlite3.sqlite')

#日志目录
LOG_PATH = os.path.join(BASE_DIR, 'logs')

# 测试集
TEST_SUITES = os.path.join(settings.BASE_DIR, 'TestCase')

if __name__ == "__main__":
    print(root_dir)