#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import os
import re

cfg_name_list = ['"showstartup-config*.txt"', '"show-*.txt"', '"showconfiguration-*.txt"']
cfg_path_list_new = []

for k in cfg_name_list:
    cfg_path = os.popen('find /home/rconfig/data -name ' + k + ' | sort').read()
    cfg_path_list = cfg_path.split('\n')

    for i in range(len(cfg_path_list)):
        if i<len(cfg_path_list)-1:
            device_name_1 = re.findall('/home/rconfig/data/[-\w\s]+/([-\w\s]+)/.*',cfg_path_list[i])
            device_name_2 = re.findall('/home/rconfig/data/[-\w\s]+/([-\w\s]+)/.*',cfg_path_list[i+1])
            if device_name_1 == device_name_2:
                continue
            else:
                cfg_path_list_new.append(cfg_path_list[i])
        else:
            cfg_path_list_new.append(cfg_path_list[i])

for j in cfg_path_list_new:
    if j:
        os.popen("cat " + j + " | sed -i ':label;N;s/\\n/ /;b label' " + j)
