#!/usr/bin/env python3
# coding=utf-8
from faker import Faker


class Fakers(object):
    def __init__(self):
        super().__init__()
        self.faker = Faker('zh_CN')

    @property
    def mobile_number(self):
        return self.faker.phone_number()  # 手机号

    @property
    def ID_card(self):
        return self.faker.ssn(min_age=1, max_age=90)  # 身份证

    @property
    def image(self):
        return self.faker.image_url()  # 图片网址

    @property
    def word(self):
        return self.faker.word()  # 随机单词

    @property
    def license_plate(self):
        return self.faker.license_plate()  # 车牌号

    @property
    def address(self):
        return self.faker.address()  # 随机地址

    @property
    def randomdate(self):
        return self.faker.date(pattern="%Y-%m-%d")  # 随机日期（可自定义格式）

    @property
    def randomtime(self):
        return self.faker.time(pattern="%H:%M")  # 随机时间（可自定义格式）

    @property
    def name(self):
        return self.faker.name()  # 生成名字


fakers = Fakers()

if __name__ == "__main__":
    print(fakers.word)
