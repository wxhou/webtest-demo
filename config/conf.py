#!/usr/bin/env python
# coding=utf-8
'''
@File    :   conf.py
@Time    :   2019/09/28 11:15:16
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys
sys.path.append('.')
import os
import platform
from utils.data_generator import gen


root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

environment = lambda x: x in platform.platform()

driver_path = os.path.join(root_dir, 'driver', 'chromedriver'
                           ) if environment('Darwin') else os.path.join(root_dir, 'driver', 'chromedriver.exe')

srceenshot_name = os.path.join(root_dir, 'screenshot', '%s.png' % gen.word)

if __name__ == '__main__':
    pass
