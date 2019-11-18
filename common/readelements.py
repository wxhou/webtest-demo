#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   readelements.py
@Time    :   2019/11/18 16:06:32
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys
sys.path.append('.')
import os
import configparser
import settings

element_path = os.path.join(settings.root_dir, 'PageElements', 'element.ini')


class Element:
    def __init__(self):
        self.element = configparser.RawConfigParser()
        self.element.read(element_path, encoding='utf-8')

    def __call__(self, *args):
        return self.element.get(*args)

    def __getattr__(self, item):
        """
        如element.Login，可以动态获取属性
        :param item:
        :return:
        """
        sections = self.element.items(item)
        if sections:
            return sections


element = Element()
if __name__ == "__main__":
    print(element('login', '密码'))
