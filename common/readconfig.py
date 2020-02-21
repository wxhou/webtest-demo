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


class ReadConfig:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read(settings.INI_PATH)

    def _get(self,*args,**kwargs):
        return self.config.get(*args,**kwargs)

    def _set(self,*args,**kwargs):
        self.config.set(*args,**kwargs)
        with open(settings.INI_PATH,'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get('server', 'url')

    @url.setter
    def url(self,value):
        self._set('server','url',value)

ini = ReadConfig()

if __name__ == '__main__':
    print(ini.url)
