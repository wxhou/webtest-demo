#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
import datetime
from functools import wraps


def run_time(func):
    """运行时间"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timestamp()
        res = func(*args, **kwargs)
        end = timestamp() - start
        print("Done! 共耗时{:.3f}秒！".format(end))
        return res

    return wrapper


def timestamp():
    """时间戳"""
    return time.time()


def now_time():
    """现在时间"""
    return datetime.datetime.now()


def datetime_strftime(fmt="%Y%m"):
    """时间线"""
    return datetime.datetime.now().strftime(fmt)


def time_strftime(end_time, fmt="%Y-%m-%d %H:%M:%S"):
    """格式化时间"""
    return time.strftime(fmt, time.localtime(end_time))  # strftime不支持中文


def sleep(seconds=1.0):
    """
    睡眠时间
    """
    time.sleep(seconds)


if __name__ == '__main__':
    print(datetime_strftime("%Y-%m-%d %H:%M:%S"))
