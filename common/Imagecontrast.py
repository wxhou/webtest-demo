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
import base64
import operator
from PIL import Image
from fuzzywuzzy import fuzz
from functools import reduce


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
    """图像对比算法"""
    def __call__(self, img1, img2):
        image1 = Image.open(img1)
        image2 = Image.open(img2)

        h1 = image1.histogram()
        h2 = image2.histogram()

        result = math.sqrt(
            reduce(operator.add, list(map(lambda a, b:
                                          (a - b)**2, h1, h2))) / len(h1))
        return result


ic = ImageContrast()
if __name__ == '__main__':
    import os
    from config.conf import root_dir

    path1 = os.path.join(root_dir, 'screenshot', '123.png')
    path2 = os.path.join(root_dir, 'screenshot', '456.png')
    img = ImageContrast()
    print(img(path1, path2))
