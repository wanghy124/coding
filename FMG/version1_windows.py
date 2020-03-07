import requests
import re
import time
import csv

# --------------------登录FGT--------------------

url_fgt = "https://139.217.218.31/logincheck"
url_fgt_vpn = "https://139.217.218.31/api/v2/monitor/vpn/ipsec/"

payload = {'username':'fgtapiuser2', 'secretkey':'Welcome01'}
requests.post(url_fgt, data=payload, verify=False)

# --------------------获取FGT数据--------------------

session_fgt = requests.session()
session_fgt.post(url_fgt, data=payload, verify=False)
response_get_fgt = session_fgt.get(url_fgt_vpn)

# --------------------处理FGT数据--------------------

device_info_fgt = response_get_fgt.text.split('proxyid')[1:]
device_pool_fgt = []

for j in device_info_fgt:
    nat_ip_fgt = re.findall('.*"subnet":"(10\.162\.\d{1,3}\.\d{1,3})-.*', j)
    mgmt_ip_fgt = re.findall('.*"rgwy":"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})".*', j)
    if nat_ip_fgt:
        device_pool_fgt.append([nat_ip_fgt[0], mgmt_ip_fgt[0]])

# --------------------登录FMG--------------------

url_fmg = "https://52.130.67.198/jsonrpc"

payload = "{\n\"id\":1,\n\"method\":\"exec\",\n\"params\":[\n{\n\"data\":{\n\"passwd\":\"Welcome01\",\n\"user\":" \
          "\"fmgapiuser2\"\n },\n\"url\":\"/sys/login/user\"\n }\n]\n}"
headers = {'Content-Type':'text/plain'}

response_login_fmg = requests.request("POST", url_fmg, headers=headers, data=payload, verify=False)

session_id = re.findall('.*"session":\s"(.*)"\s}',response_login_fmg.text)

# --------------------获取FMG数据--------------------

payload = "{\n\"method\":\"get\",\n \"params\":[\n{\n\"meta fields\":[\n\"\"\n],\n\"url\":\"/dvmdb/device\"\n}\n],\n" \
          "\"session\": \"" + session_id[0] + "\",\n\"id\":1\n}"
headers = {'Content-Type':'text/plain'}

response_get_fmg = requests.request("POST", url_fmg, headers=headers, data=payload, verify=False)

# --------------------处理FMG数据--------------------

device_info_fmg = response_get_fmg.text.split('adm_pass')

now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time()))
fname = now + r"_fmg_report.csv"

with open(fname, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Status"])
    for i in device_info_fmg:
        hostname = re.findall('.*"hostname":\s+"(FGT\w+)",\s+.*', i)
        conn_status = re.findall('.*"conn_status":\s+(\d),\s+.*', i)
        mgmt_if = re.findall('.*"mgmt_if":\s+"(wan|wwan)",\s+.*', i)
        if hostname:
            if conn_status[0] == '1' and mgmt_if[0] == 'wan':
                writer.writerow([hostname[0], 'Good'])
            elif conn_status[0] == '1' and mgmt_if[0] == 'wwan':
                mgmt_ip_fmg = re.findall('.*"ip":\s+"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",\s+.*', i)
                nat_ip_fmg = re.findall('.*"var06_nat_ip":\s+"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",\s+.*', i)
                if [nat_ip_fmg[0], mgmt_ip_fmg[0]] in device_pool_fgt:
                    writer.writerow([hostname[0], '4G'])
                else:
                    writer.writerow([hostname[0], 'Good'])
            elif conn_status[0] == '2':
                writer.writerow([hostname[0], 'Offline!'])
            else:
                writer.writerow([hostname[0], 'Null'])

# --------------------登出FMG--------------------

payload = "{\n\"id\":1,\n\"jsonrpc\":\"1.0\",\n\"method\":\"exec\",\n\"params\":[\n{\n\n\"url\":\"/sys/logout\"\n}\n],\n" \
          "\"session\": \"" + session_id[0] + "\",\n\"verbose\":1\n}"
headers = {}
requests.request("POST", url_fmg, headers=headers, data=payload, verify=False)

