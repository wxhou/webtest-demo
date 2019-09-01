#!/usr/bin/env python3
# coding=utf-8
import configparser
import os

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
ini_path = os.path.join(root_dir, 'config', 'config.ini')
element_path = os.path.join(root_dir, 'config', 'element.ini')


class ReadConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(ini_path)

    @property
    def url(self):
        return self.config.get('server', 'url')

    @property
    def remote_state(self):
        state = self.config.get('remote', 'state')
        return state

    @property
    def remote_server(self):
        server = self.config.get('remote', 'server')
        return server

    @remote_state.setter
    def remote_state(self, value):
        self.config.set('remote', 'state', value)
        with open(ini_path, 'w', encoding='utf-8') as f:
            self.config.write(f)


class Element:

    def __init__(self):
        self.element = configparser.ConfigParser()
        self.element.read(element_path, encoding='utf-8')

    def __call__(self, *args):
        return self.element.get(*args)

    def __getattr__(self, item):
        """
        如element.Login，可以动态获取属性
        :param item:
        :return:
        """
        sections = self.element.items(item)
        return sections


if __name__ == '__main__':
    print(root_dir)
    element = Element()
    print(element('login', '账号'))
