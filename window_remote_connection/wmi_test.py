#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'LiTian'


import wmi

def sys_version(ip_address, user, password):
    conn = wmi.WMI(computer=ip_address, user=user, password=password)
    for sys in conn.Win32_OperatingSystem():
        print('Version:%s' % sys.Caption.encode('UTF8'))
        print(sys.OSArchitecture.encode("UTF8"))
        print(sys.NumberOfProcesses)


if __name__ == '__main__':
    sys_version(ip_address='192.168.1.252', user='administrator', password='yunrun2017!@#')
