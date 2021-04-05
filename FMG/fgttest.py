import requests
import re

# --------------------登录FGT--------------------

url_fgt = "https://139.217.218.31/logincheck"
url_fgt_vpn = "https://139.217.218.31/api/v2/monitor/vpn/ipsec/"

payload = {'username':'fgtapiuser2', 'secretkey':'Welcome01'}
requests.post(url_fgt, data=payload, verify=False)

# --------------------获取FGT数据--------------------

session_fgt = requests.session()
session_fgt.post(url_fgt, data=payload, verify=False)
response_get_fgt = session_fgt.get(url_fgt_vpn)
print(response_get_fgt.text)
# --------------------处理FGT数据--------------------

# device_info_fgt = response_get_fgt.text.split('proxyid')[1:]
# device_pool_fgt = {}
#
# for j in device_info_fgt:
#     nat_ip_fgt = re.findall('.*"subnet":"(10\.162\.\d{1,3}\.\d{1,3})-.*', j)
#     tun_ip_fgt = re.findall('.*"subnet":"100\.(10[1-2])\.\d{1,3}\.\d{1,3}-.*', j)
#     if tun_ip_fgt:
#         device_pool_fgt[nat_ip_fgt[0]] = tun_ip_fgt[0]
#
# print(device_pool_fgt)

# for j in device_info_fgt:
#     nat_ip_fgt = re.findall('.*"subnet":"(10\.162\.\d{1,3}\.\d{1,3})-.*', j)
#     mgmt_ip_fgt = re.findall('.*"rgwy":"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})".*', j)
#     if nat_ip_fgt:
#         device_pool_fgt.append([nat_ip_fgt[0], mgmt_ip_fgt[0]])
