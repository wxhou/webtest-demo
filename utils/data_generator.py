#!/usr/bin/env python3
# coding=utf-8
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
