#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'LiTian'

import paramiko,os,sys


def ssh_cmd(ip, port, cmd, user, passwd):
    result = ""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, user, passwd)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        print(result)
        ssh.close()
        return result
    except Exception as e:
        print("ssh_cmd err:%s" % e)


if __name__ == '__main__':
    print(ssh_cmd('221.204.232.4', '23332', 'dir', 'administrator', 'urunadmin2017!@#'))
