#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import yaml


class Element:
    """获取元素"""

    def __init__(self, route, name):
        self.path = os.path.join(route, '%s.yaml' % name)
        if not os.path.exists(self.path):
            raise FileNotFoundError("%s 文件不存在！" % self.path)
        with open(self.path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f.read())

    def __getitem__(self, item):
        return self.data[item]


if __name__ == '__main__':
    pass
