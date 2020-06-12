#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import os
import yaml
from config.conf import ELEMENT_PATH


class Element:
    """获取元素"""

    def __init__(self, name):
        self.path = os.path.join(ELEMENT_PATH, '%s.yaml' % name)
        if not os.path.exists(self.path):
            raise FileNotFoundError("%s 文件不存在！" % self.path)
        with open(self.path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f.read())

    def __getitem__(self, item):
        return self.data[item]


if __name__ == '__main__':
    login = Element('login')
    print(login['登录'])
