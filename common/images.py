#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import os
import time
import settings
from PIL import Image
from utils.logger import Logger

log = Logger('image').logger


def element_screenshot(locator, path):
    """元素截图"""
    log.warning("需要截图的元素坐标%s" % locator.location)
    log.warning("需要截图的元素大小%s" % locator.size)
    shot = (locator.location['x'], locator.location['y'],
            locator.location['x'] + locator.size['width'],
            locator.location['y'] + locator.size['height'])
    im = Image.open(path)
    im = im.crop(shot)
    im.save(path)
    time.sleep(1)


def get_image_name(string):
    """获取文件名称"""
    pattern = re.compile(r'([^<>/\\\|:""\*\?]+)\.\w+$')
    return pattern.findall(string)


def get_airtest_image(name):
    """获取airtest图像"""
    _path = settings.AIRTEST_PATH
    return os.path.join(_path, f"{name}.png")


if __name__ == '__main__':
    pass
