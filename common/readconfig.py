#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import configparser
import settings

SERVER = 'server'
URL = 'url'


class ReadConfig:
    def __init__(self):
        self.path = settings.INI_PATH
        self.config = configparser.RawConfigParser()
        self.config.read(self.path)

    def _get(self, section, option):
        """得到"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """获取"""
        self.config.set(section, option, value)
        with open(self.path, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(SERVER, URL)

    @url.setter
    def url(self, value):
        self._set(SERVER, URL, value)


ini = ReadConfig()

if __name__ == '__main__':
    print(ini.url)
