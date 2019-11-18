#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   data_generator.py
@Time    :   2019/11/18 15:20:54
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys
sys.path.append('.')
import os
import settings
from faker import Factory

faker = Factory().create('zh_CN')


class Generator:
    @property
    def mobile_number(self):
        return faker.phone_number()  # 手机号

    @property
    def ID_card(self):
        return faker.ssn(min_age=1, max_age=90)  # 身份证

    @property
    def image(self):
        return faker.image_url()  # 图片网址

    @property
    def word(self):
        return faker.word()  # 随机单词

    @property
    def license_plate(self):
        return faker.license_plate()  # 车牌号

    @property
    def address(self):
        return faker.address()  # 随机地址

    @property
    def randomdate(self):
        return faker.date(pattern="%Y-%m-%d")  # 随机日期（可自定义格式）

    @property
    def randomtime(self):
        return faker.time(pattern="%H:%M")  # 随机时间（可自定义格式）

    @property
    def name(self):
        return faker.name()  # 生成名字

    @property
    def screen_expected(self):
        """预期图片"""
        screen_name = os.path.join(settings.root_dir, 'screenshot',
                                   'Expected.png')
        return screen_name
    @property
    def screenshot_name(self):
        """截图名称"""
        return os.path.join(settings.root_dir, 'screenshot', '%s.png' % gen.word)


gen = Generator()

if __name__ == "__main__":
    print(gen.address)