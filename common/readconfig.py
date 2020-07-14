#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import configparser

HOST = 'HOST'


class ReadConfig:
    def __init__(self, route):
        self.path = os.path.join(route, 'config.ini')
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
        return self._get(HOST, HOST)


if __name__ == '__main__':
    pass
