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

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Dirty:
    def __init__(self):
        self.end_time = time.time() - 1 * 24 * 3600
        self.timeline = time.strftime("%Y年%m月%d日%H时%M分%S秒",
                                      time.localtime(self.end_time))
        print("当前删除的时间线是：%s" % self.timeline)

    def __call__(self):
        """删除生成的图片脏数据"""
        png_path = os.path.join(root_dir, 'screenshot')
        ver = True
        for i in os.listdir(png_path):
            if i.endswith('.png'):
                start_time = os.path.getmtime(os.path.join(png_path, i))
                if start_time < self.end_time:
                    delete_pic = os.path.join(png_path, i)
                    os.remove(delete_pic)
                    print("删除%s完毕！"%delete_pic)
                    ver = False
        if ver:
            print("当前没有删除任何脏数据！")



dirty_data = Dirty()

if __name__ == '__main__':
    dirty_data()