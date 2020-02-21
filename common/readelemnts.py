#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   readyaml.py
@Time    :   2019/09/28 11:52:25
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys
sys.path.append('.')
import os
import yaml
import settings


class Element:
    """获取元素"""
    def __init__(self, name):
        self.element = os.path.join(settings.ELEMENT_PATH, '%s.yaml' % name)
        if not os.path.exists(self.element):
            raise FileNotFoundError("%s 文件不存在！" % self.element)
        with open(self.element, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __call__(self, item):
        """获取定位元素值"""
        return self.data[item]


if __name__ == '__main__':
    login = Element('login')
    print(login('登录'))