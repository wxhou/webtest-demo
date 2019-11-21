#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   dbconnect.py
@Time    :   2019/09/28 11:11:44
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys
sys.path.append('.')
import os
import sqlite3

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class SQLite:
    def __init__(self):
        db_path = os.path.join(root_dir, 'database', 'sqlite3.sqlite')
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()

    def __enter__(self):
        """
        with as 语句打开数据库
        :return:
        """
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.commit()
        self.cur.close()
        self.con.close()


if __name__ == '__main__':
    with SQLite() as f:
        f.execute('select * from STUDENT;')
        data = f.fetchall()
    print(data)
