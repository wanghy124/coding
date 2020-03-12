#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from c11_2 import *
from c11_3 import *

def ping_ssh(ip_list, username, password, cmd):
    for ip in ip_list:
        ping_result = pings(ip)
        if ping_result[1] == 1:
            print(ping_result[0],'good')
            print(paramiko_ssh(ip, username=username,password=password,cmd=cmd))
        else:
            print(ping_result[0],'bad')

if __name__ == '__main__':
    ip_list = ['192.168.27.100','192.168.27.99']
    ping_ssh(ip_list, 'root', 'cisco', 'ls')

