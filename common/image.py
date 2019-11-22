#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   Imagecontrast.py
@Time    :   2019/09/28 11:07:57
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys
sys.path.append('.')
import math
import time
import base64
import operator
from PIL import Image
from fuzzywuzzy import fuzz
from functools import reduce
from utils.log import log

class BaseComparison:
    """通过base64字符串对比图像"""

    def comparison(self, path):
        with open(path, 'rb') as f:
            basedata = base64.b64encode(f.read())
        return basedata

    def calc_similar(self, path1, path2):
        li, ri = self.comparison(path1), \
                 self.comparison(path2)
        if fuzz.ratio(li, ri) > 90:
            return True
        else:
            return False


class ImageContrast:
    """图像对比算法，当result为0.0时结果正确"""
    def element_shot(self, locator, path):
        """元素截图"""
        log.warning("需要截图的元素坐标%s" % locator.location)
        log.warning("需要截图的元素大小%s" % locator.size)
        shot = (locator.location['x'],
                locator.location['y'],
                locator.location['x'] + locator.size['width'],
                locator.location['y'] + locator.size['height'])
        im = Image.open(path)
        im = im.crop(shot)
        im.save(path)
        time.sleep(1)

    def __call__(self, img1, img2):
        image1 = Image.open(img1)
        image2 = Image.open(img2)

        h1 = image1.histogram()
        h2 = image2.histogram()

        result = math.sqrt(
            reduce(operator.add, list(map(lambda a, b:
                                          (a - b)**2, h1, h2))) / len(h1))
        return result


pic = ImageContrast()
if __name__ == '__main__':
    import os
    from settings import root_dir
    path1 = os.path.join(root_dir, 'screenshot', 'Expected.png')
    path2 = os.path.join(root_dir, 'screenshot', '有些.png')
    img = BaseComparison()
    print(img.calc_similar(path1, path2))
