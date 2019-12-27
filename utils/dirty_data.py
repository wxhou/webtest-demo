#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   dirty_data.py
@Time    :   2019/09/28 11:11:11
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys
sys.path.append('.')
import os
import time
import settings


class Dirty:
    def __init__(self):
        self.end_time = time.time() - 1 * 24 * 3600
        self.timeline = time.strftime("%Y-%m-%d %H:%M:%S",
                                      time.localtime(
                                          self.end_time))  # strftime不支持中文
        print("当前删除的时间线是：%s" % self.timeline)

    def __call__(self):
        """删除生成的图片脏数据"""
        ver = True
        for i in os.listdir(settings.SCREENSHOT_PATH):
            if i.endswith('.png'):
                start_time = os.path.getmtime(
                    os.path.join(settings.SCREENSHOT_PATH, i))
                if start_time < self.end_time:
                    delete_pic = os.path.join(png_path, i)
                    os.remove(delete_pic)
                    print("删除%s完毕！" % delete_pic)
                    ver = False
        if ver:
            print("当前没有删除任何脏数据！")


dirty_data = Dirty()

if __name__ == '__main__':
    dirty_data()