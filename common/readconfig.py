#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import configparser
from config.conf import INI_PATH

HOST = 'HOST'


class ReadConfig:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read(INI_PATH)

    def _get(self, section, option):
        """得到"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """获取"""
        self.config.set(section, option, value)
        with open(INI_PATH, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(HOST, HOST)


ini = ReadConfig()

if __name__ == '__main__':
    print(ini.url)
