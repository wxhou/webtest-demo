#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from airtest_selenium.exceptions import IsNotTemplateError


def get_image(route, name):
    """获取airtest图像"""
    path = os.path.join(route, "{}.png".format(name))
    if os.path.exists(path):
        return path
    raise IsNotTemplateError("验证图片不存在：{}".format(path))
