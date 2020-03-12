#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import logging
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)
from kamene.all import *

def pings(dst_ip):
    ping_pkt = IP(dst=dst_ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return dst_ip,1
    else:
        return dst_ip,2

if __name__ == '__main__':
    result = pings('192.168.27.2')
    if result[1] == 1:
        print(result[0],'good')
    else:
        print(result[0],'bad')


