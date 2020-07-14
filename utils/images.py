#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import math
import operator
from PIL import Image
from functools import reduce
from utils.logger import log
from utils.times import sleep


def area_screenshot(locator, path):
    """区域截图"""
    log.warning("需要截图的元素坐标%s" % locator.location)
    log.warning("需要截图的元素大小%s" % locator.size)
    shot = (locator.location['x'], locator.location['y'],
            locator.location['x'] + locator.size['width'],
            locator.location['y'] + locator.size['height'])
    im = Image.open(path)
    im = im.crop(shot)
    im.save(path)
    sleep()


def get_image_name(string):
    """获取文件名称"""
    pattern = re.compile(r'([^<>/\\\|:""\*\?]+)\.\w+$')
    return pattern.findall(string)


def image_contrast_result(img1path, img2path, threshold=0.7):
    """图像对比结果"""
    image1 = Image.open(img1path)
    image2 = Image.open(img2path)

    h1 = image1.histogram()
    h2 = image2.histogram()

    result = math.sqrt(
        reduce(operator.add, list(map(lambda a, b:
                                      (a - b) ** 2, h1, h2))) / len(h1))
    # result完全相等是0.0，设置阈值为0.7
    print("图像对比结果是：{}".format(result))
    return result < threshold


if __name__ == '__main__':
    print(
        image_contrast_result(
            '/Users/hoou/PycharmProjects/webtest-demo/airtest_img/CMS管理.png',
            '/Users/hoou/PycharmProjects/webtest-demo/airtest_img/头像.png',
        ))
