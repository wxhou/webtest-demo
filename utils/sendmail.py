#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

sys.path.append('.')
import os
import conf
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart


def get_new_report():
    """获取最新的报告"""
    report_path = os.listdir(conf.REPORT_PATH)
    report_new_path = sorted(report_path, key=lambda x: os.path.getmtime(os.path.join(conf.REPORT_PATH, x)))
    report_new_file = os.path.join(conf.REPORT_PATH, report_new_path[-1])
    with open(report_new_file, encoding='utf-8') as f:
        return f.read()


def _format_addr(s):
    """格式化邮件地址"""
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_report_mail():
    """发送最新的测试报告"""
    # email地址和口令：
    user = '1084502012@qq.com'
    pwd = 'cmzwajsrkujagbha'
    # 收件人地址
    to_addr = ['1084502012@qq.com', 'wxhou@yunjinginc.com']
    # SMTP服务器地址
    smtp_server = 'smtp.qq.com'
    smtp_port = 465
    try:
        # 初始化邮件对象
        msg = MIMEMultipart()
        msg['From'] = _format_addr("selenium爱好者<%s>" % user)
        msg['To'] = _format_addr('管理员 <%s>' % ','.join(to_addr))
        msg['Subject'] = Header("unittest演示测试最新的测试报告", 'utf-8').encode()

        # 发送HTML文件
        msg.attach(MIMEText(get_new_report(), 'html', 'utf-8'))

        # 发件人邮箱中的SMTP服务器，端口是994(网易企业邮箱)
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            # 括号中对应的是发件人邮箱账号、邮箱密码
            server.login(user, pwd)
            # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.sendmail(user, to_addr, msg.as_string())
        print("测试结果邮件发送成功！")
    except smtplib.SMTPException as e:
        print(u"Error: 无法发送邮件", format(e))


if __name__ == '__main__':
    print(get_new_report())
    send_report_mail()
