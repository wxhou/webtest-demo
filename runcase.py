#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import os
import conf
import unittest
from utils.sendmail import send_report_mail
from utils.times import datetime_strftime
from utils.clear_data import clear_old_data
from utils.HTMLTestRunner_cn import HTMLTestRunner

discover = unittest.defaultTestLoader.discover(conf.TEST_SUITES, pattern="test*.py")


def report_path():
    """报告文件"""
    if not os.path.exists(conf.REPORT_PATH):
        os.makedirs(conf.REPORT_PATH)
    return os.path.join(conf.REPORT_PATH, '{}.html'.format(datetime_strftime("%Y%m%d_%H%M%S")))


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
    finally:
        clear_old_data(conf.BASE_DIR)
        send_report_mail()
