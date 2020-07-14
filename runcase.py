#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import unittest
from config import tests, REPORT_DIR
from utils.sendmail import send_report_mail
from utils.times import datetime_strftime
from script.HTMLTestRunner_cn import HTMLTestRunner

TEST_DIR = tests['zentao']
discover = unittest.defaultTestLoader.discover(TEST_DIR, pattern="test*.py")


def report_path():
    """报告文件"""
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)
    return os.path.join(REPORT_DIR, '{}.html'.format(datetime_strftime("%Y%m%d_%H%M%S")))


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
        print("用例执行失败:{}".format(e))
        send_report_mail()
