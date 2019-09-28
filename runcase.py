#!/usr/bin/env python
# coding=utf-8
'''
@File    :   runcase.py
@Time    :   2019/09/28 11:20:56
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys
sys.path.append('.')
import os
import unittest
from config.conf import root_dir
from utils.HTMLTestRunner_cn import HTMLTestRunner


def report_path():
    """报告目录"""
    report_path = os.path.join(root_dir, 'report')
    if not os.path.exists(report_path):
        os.makedirs(report_path)
    return os.path.join(report_path, 'report.html')


test_suites = os.path.join(root_dir, 'TestCase')
discover = unittest.defaultTestLoader.discover(test_suites, pattern="test*.py")

if __name__ == "__main__":
    try:
        with open(report_path(), 'wb+') as fp:
            runner = HTMLTestRunner(stream=fp,
                                    title="测试结果",
                                    description="用例执行情况",
                                    verbosity=2,
                                    retry=1,
                                    save_last_try=True)
            runner.run(discover)
    except Exception as e:
        print("用例执行失败", format(e))
