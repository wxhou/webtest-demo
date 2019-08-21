#!/usr/bin/env python3
# coding=utf-8
import os
import platform
from utils.data_generator import Generator

gen = Generator()

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

environment = lambda x: x in platform.platform()

driver_path = os.path.join(root_dir, 'driver', 'chromedriver'
                           ) if environment('Darwin') else os.path.join(root_dir, 'driver', 'chromedriver.exe')

srceenshot_name = os.path.join(root_dir, 'screenshot', '%s.png' % gen.word)

if __name__ == '__main__':
    pass
