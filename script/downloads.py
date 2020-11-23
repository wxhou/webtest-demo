#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import urllib3
import requests

urllib3.disable_warnings()


class Download(object):
    """下载"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    }

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def fast_load(self):
        """快速下载"""
        r = requests.get(self.url, headers=self.headers)
        with open(self.path, 'wb') as f:
            f.write(r.content)

    def slow_load(self, chunk_size=1024):
        """慢速下载"""
        r = requests.get(self.url, headers=self.headers, stream=True)
        data_count = 0
        content_size = int(r.headers['content-length'])
        with open(self.path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                data_count = data_count + len(chunk)
                now_jd = (data_count / content_size) * 100
                print("\r 文件下载进度：%d%%(%d/%d) - %s" %
                      (now_jd, data_count, content_size, self.path), end=" ")


if __name__ == '__main__':
    pass
