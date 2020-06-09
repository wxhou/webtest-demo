#!/usr/bin/env python3
# coding=utf-8
import sys

sys.path.append('.')
import os
from config import conf


def clear_old_data(filepath):
    """清除脏数据"""
    # end_time = timestamp() - 1 * 24 * 3600
    # timeline = time_strftime(end_time)
    # print("当前删除的时间线是：%s" % timeline)
    ver = True
    for i in os.listdir(filepath):
        filename = os.path.join(filepath, i)
        if os.path.isfile(filename) and any([i.endswith(x) for x in ['.png', '.jpg']]):
            delete_pic = os.path.join(filepath, i)
            # start_time = os.path.getmtime(delete_pic)
            # if start_time < end_time:
            os.remove(delete_pic)
            print("删除%s完毕！" % delete_pic)
            ver = False
    if ver:
        print("当前目录:{}".format(filepath))
        print("当前没有删除任何脏数据！")


if __name__ == '__main__':
    # clear_old_data(conf.TEST_SUITES)
    clear_old_data(conf.BASE_DIR)
