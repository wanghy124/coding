# l1 = [4,5,7,1,3,9,0]
# l2 = l1.copy()
# l2.sort()
# print(l1)
# print(l2)
# for i in range(len(l1)):
#     print(l1[i],l2[i])

import os
import re

str1 = os.popen('ifconfig '+'ens33').read()
list1 = str1.split('\n')

for i in range(len(list1)):
    IP_Addr = re.findall('inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+',list1[i])
    if IP_Addr:
        print('{:<10s}:{:<10s}'.format('IP_Addr',IP_Addr[0]))

for i in range(len(list1)):
    Netmask = re.findall('netmask\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+',list1[i])
    if Netmask:
        print('{:<10s}:{:<10s}'.format('Netmask',Netmask[0]))

for i in range(len(list1)):
    Broadcast = re.findall('broadcast\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*',list1[i])
    if Broadcast:
        print('{:<10s}:{:<10s}'.format('Broadcast',Broadcast[0]))

for i in range(len(list1)):
    Mac_Addr = re.findall('\s*(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})\s*',list1[i])
    if Mac_Addr:
        print('{:<10s}:{:<10s}'.format('Mac_Addr',Mac_Addr[0]))

