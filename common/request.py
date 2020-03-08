#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import requests
import urllib3

urllib3.disable_warnings()


class Download:
    """下载"""

    def __init__(self, url, path, stream=False):
        self.url = url
        self.path = path
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }
        self.r = requests.get(url, headers=self.headers, stream=stream)

    def fast_load(self):
        """快速下载"""
        with open(self.path, 'wb') as f:
            f.write(self.r.content)
        return self.path

    def slow_load(self):
        """慢速下载"""
        chunk_size = 1024
        content_size = int(self.r.headers['content-length'])
        data_count = 0
        with open(self.path, 'wb') as f:
            for chunk in self.r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                data_count = data_count + len(chunk)
                now_jd = (data_count / content_size) * 100
                print("\r 文件下载进度：%d%%(%d/%d) - %s" % (now_jd, data_count, content_size, self.path), end=" ")


if __name__ == '__main__':
    pass
