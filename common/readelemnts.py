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

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
element_path = lambda x: os.path.join(root_dir, 'PageElements', '{}.yaml'.
                                      format(x))


class Element:
    """获取元素"""
    def __init__(self, name):
        if not os.path.exists(element_path(name)):
            raise FileNotFoundError("%s 文件不存在！" % element_path(name))
        with open(element_path(name), encoding='utf-8') as f:
            self.data = yaml.safe_load(f.read())

    def __getattr__(self, item):
        sections = self.data.get(item)
        if sections:
            return sections
        else:
            raise ValueError("关键字 %s 获取元素结果为空" % item)


if __name__ == '__main__':
    login = Element('login')
    print(login.登录)