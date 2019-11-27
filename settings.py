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
root_dir = os.path.abspath(os.path.dirname(__file__))

#系统环境
environment = lambda x: x in platform.platform()

if __name__ == "__main__":
    print(root_dir)