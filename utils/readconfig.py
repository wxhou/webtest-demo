#!/usr/bin/env python3
# coding=utf-8
import configparser
import os
from config.conf import root_dir


class ReadConfig:
    def __init__(self):
        config_path = os.path.join(root_dir, 'config', 'config.ini')
        self.config = configparser.ConfigParser()
        data =  self.config.read(config_path)
        print(data)

if __name__ == '__main__':
    ReadConfig()