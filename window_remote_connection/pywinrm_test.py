#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'LiTian'

import winrm
import sys

host = '221.204.232.4'
username = 'administrator'
password = 'urunadmin2017!@#'

s = winrm.Session('http://' + host + ':5985/wsman', auth=(username, password))


def _runCommand(comm):
    if comm == 'q':
        sys.exit()
    r = s.run_cmd(comm)
    print(r.std_out)


while 1:
    comm = input("command>>")
    _runCommand(comm)