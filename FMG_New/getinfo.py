import requests
import re
import os
import time
import csv

# --------------------登录FMG--------------------

url = "https://52.130.67.198/jsonrpc"

payload = "{\n\"id\":1,\n\"method\":\"exec\",\n\"params\":[\n{\n\"data\":{\n\"passwd\":\"Welcome01\",\n\"user\":" \
          "\"fmgapiuser2\"\n },\n\"url\":\"/sys/login/user\"\n }\n]\n}"
headers = {'Content-Type':'text/plain'}

response_login = requests.request("POST", url, headers=headers, data=payload, verify=False)

session_id = re.findall('.*"session":\s"(.*)"\s}',response_login.text)

# --------------------获取数据--------------------

payload = "{\n\"method\":\"get\",\n \"params\":[\n{\n\"meta fields\":[\n\"\"\n],\n\"url\":\"/dvmdb/device\"\n}\n],\n" \
          "\"session\": \"" + session_id[0] + "\",\n\"id\":1\n}"
headers = {'Content-Type':'text/plain'}

response_get = requests.request("POST", url, headers=headers, data=payload, verify=False)

# --------------------处理数据--------------------

device_info = response_get.text.split('adm_pass')

now = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time()))
fname = now + r"_fmg_report.csv"
# file = open(fname,'w')
with open(fname, "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Status"])
    for i in device_info:
        hostname = re.findall('.*"hostname":\s+"(FGT\w+)",\s+.*', i)
        conn_status = re.findall('.*"conn_status":\s+(\d),\s+.*', i)
        mgmt_if = re.findall('.*"mgmt_if":\s+"(wan|wwan)",\s+.*', i)
        if hostname:
            if conn_status[0] == '1' and mgmt_if[0] == 'wan':
                writer.writerow([hostname[0], 'Good'])
            elif conn_status[0] == '1' and mgmt_if[0] == 'wwan':
                writer.writerow([hostname[0], '4G'])
            elif conn_status[0] == '2':
                writer.writerow([hostname[0], 'Offine!'])
            else:
                writer.writerow([hostname[0], 'Null'])


