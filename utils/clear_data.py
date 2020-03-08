#!/usr/bin/env python3
# coding=utf-8
import sys

sys.path.append('.')
import os
import time
import settings


def clear_old_data(filepath):
    """清除脏数据"""
    end_time = time.time() - 1 * 24 * 3600
    timeline = time.strftime("%Y-%m-%d %H:%M:%S",
                             time.localtime(end_time))  # strftime不支持中文
    print("当前删除的时间线是：%s" % timeline)
    ver = True
    for i in os.listdir(filepath):
        if any([i.endswith(x) for x in ('.png', '.jpg')]):
            delete_pic = os.path.join(filepath, i)
            start_time = os.path.getmtime(delete_pic)
            if start_time < end_time:
                os.remove(delete_pic)
                print("删除%s完毕！" % delete_pic)
                ver = False
    if ver:
        print("当前没有删除任何脏数据！")


if __name__ == '__main__':
    clear_old_data(settings.TEST_SUITES)
