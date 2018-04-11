#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'LiTian'

from win32com.client import GetObject

wmi = GetObject('winmgmts:')
processes = wmi.ExecQuery('Select * from Win32_Process')
for process in processes:
    print(process.ProcessID, process.Name)
