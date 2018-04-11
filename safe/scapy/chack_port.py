#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
检查端口开放情况
"""

__author__ = 'LiTian'

from scapy.all import *


def synscan(domain, port):
    result = sr1(IP(dst=domain) / TCP(dport=port, flags="S"), timeout=5)
    value = 'close'
    if result:
        if result[TCP].flags==18:
            value = 'open'
    print('%s:%s,%s' % (domain, port, value))


if __name__ == '__main__':
    synscan('192.168.1.238', 18080)
