import re

str1 = 'Port-channel1.189          192.168.189.254  YES     CONFIG   up                       up '
str2 = 'Loopback4                  100.12.255.200  YES NVRAM  up                    up'
str3 = 'GigabitEthernet0/1.2523    220.248.8.2     YES NVRAM  down                    up      ' \
       'GigabitEthernet0/1.2595    27.115.48.198   YES NVRAM  up                    up      '

result1 = re.match('\s*(\w.*\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w*\s+\w*\s+(up|down).*',str1).groups()
result2 = re.match('\s*(\w.*\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w*\s+\w*\s+(up|down).*',str2).groups()
result3 = re.match('\s*([A-Za-z0-9./]*)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w*\s+\w*\s+(up|down)\s+\w\s*',str3).groups()

print('-'*100)
# print('{:<10s}：{:<10s}'.format('接口',result1[0]))
# print('{:<10s}：{:<10s}'.format('IP地址',result1[1]))
# print('{:<10s}：{:<10s}'.format('状态',result1[2]))
# print('{:<10s}：{:<10s}'.format('接口',result2[0]))
# print('{:<10s}：{:<10s}'.format('IP地址',result2[1]))
# print('{:<10s}：{:<10s}'.format('状态',result2[2]))



