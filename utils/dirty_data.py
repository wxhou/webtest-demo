#!/usr/bin/env python3
# coding=utf-8
import os
import time

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Dirty:
    def __init__(self):
        self.end_time = time.time() - 7 * 24 * 3600
        self.timeline = time.strftime("%Y年%m月%d日%H时%M分%S秒",
                                      time.localtime(self.end_time))
        print("当前删除的时间线是：%s" % self.timeline)

    def delete_png(self):
        """删除生成的图片脏数据"""
        png_path = os.path.join(root_dir, 'screenshot')
        for i in os.listdir(png_path):
            if i.endswith('.png'):
                start_time = os.path.getmtime(os.path.join(png_path, i))
                print(start_time)
                if start_time < self.end_time:
                    os.remove(os.path.join(png_path, i))
        else:
            print("图片脏数据删除完毕！")


if __name__ == '__main__':
    a = Dirty()
    print(a.delete_png())
