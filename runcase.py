#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import conf
import unittest
from utils.times import now_time
from utils.clear_data import clear_old_data
from utils.HTMLTestRunner_cn import HTMLTestRunner

discover = unittest.defaultTestLoader.discover(conf.TEST_SUITES, pattern="test*.py")

if __name__ == "__main__":
    try:
        with open('report/{}.html'.format(now_time()), 'wb+') as fp:
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
