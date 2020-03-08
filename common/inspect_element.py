#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import os
import yaml
import time
import settings
from Page.webpage import LOCATE_MODE


def inspect_element():
    """审查所有的元素是否正确"""
    path = settings.ELEMENT_PATH
    start_time = time.time()
    for i in os.listdir(path):
        _dir = os.path.join(path, i)
        if os.path.isfile(_dir):
            with open(_dir) as f:
                data = yaml.safe_load(f)
                for k in data:
                    ele = data[k]
                    if "==" in ele:
                        pattern, value = ele.split('==')
                        if pattern not in LOCATE_MODE:
                            raise AttributeError('【%s】路径中【%s]元素没有指定类型' %
                                                 (i, k))
                        if pattern == 'xpath':
                            assert '//' in ele, '【%s】路径中【%s]元素xpath类型与值不配' % (
                                i, k)
                        if pattern == 'css':
                            assert '//' not in ele, '【%s】路径中【%s]元素css类型与值不配' % (
                                i, k)
                    else:
                        raise AttributeError('【%s】路径中【%s]元素没有指定元素分隔符' % (i, k))
    end_time = time.time()
    print("校验元素done！用时%.3f秒！" % (end_time - start_time))


if __name__ == '__main__':
    inspect_element()
