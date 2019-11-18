#!/usr/bin/env python3
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
import settings
import os

ini_path = os.path.join(settings.root_dir, 'config.ini')


class ReadConfig:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read(ini_path)

    @property
    def url(self):
        return self.config.get('server', 'url')


ini = ReadConfig()

if __name__ == '__main__':
    print(ini.url)
