#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import site

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
USER_PTH = os.path.join(site.getsitepackages()[0], 'requirements.pth')


def main():
    try:
        os.remove(USER_PTH)
        print("删除文件：", USER_PTH)
    except FileNotFoundError:
        pass
    if os.path.exists(USER_PTH):
        print("文件已存在：%s" % USER_PTH)
        return
    with open(USER_PTH, 'w') as f:
        f.write(BASE_DIR)
        print("生成文件成功：", USER_PTH)
        print("文件位置：%s" % USER_PTH)
    with open(USER_PTH) as f:
        print("文件内容：%s" % f.read())


if __name__ == '__main__':
    main()
