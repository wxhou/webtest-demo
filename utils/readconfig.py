#!/usr/bin/env python
# coding=utf-8
'''
@File    :   readconfig.py
@Time    :   2019/09/28 11:08:34
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys
sys.path.append('.')
import configparser
import os

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
ini_path = os.path.join(root_dir, 'config', 'config.ini')
element_path = os.path.join(root_dir, 'config', 'element.ini')


class ReadConfig:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read(ini_path)

    @property
    def url(self):
        return self.config.get('server', 'url')


class Element:
    def __init__(self):
        self.element = configparser.ConfigParser()
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


conf = ReadConfig()
element = Element()

if __name__ == '__main__':
    print(root_dir)
    print(element.se)
