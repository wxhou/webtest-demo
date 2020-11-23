#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from config import *
from common.readconfig import ReadConfig


# 测试应用管理
apps = {
    'zentao': os.path.join(BASE_DIR, 'apps', 'zentao')
}

# 测试配置文件管理
ini = {
    'zentao': ReadConfig(apps['zentao'])
}

# 测试元素管理
element = {
    'zentao': os.path.join(apps['zentao'], 'page', 'elements')
}

# 测试图片管理
airimages = {
    'zentao': os.path.join(apps['zentao'], 'page', 'images')
}

# 测试集
tests = {
    'zentao': os.path.join(apps['zentao'], 'tests')
}

if __name__ == "__main__":
    print(BASE_DIR)
    print(ini['zentao'].url)
