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
device_pool_fgt = {}
nat_ip_pool_fgt = []

for j in device_info_fgt:
    nat_ip_fgt = re.findall('.*"subnet":"(10\.162\.\d{1,3}\.\d{1,3})-.*', j)
    tun_ip_fgt = re.findall('.*"subnet":"100\.(10[1-2])\.\d{1,3}\.\d{1,3}-.*', j)
    if tun_ip_fgt:
        device_pool_fgt[nat_ip_fgt[0]] = tun_ip_fgt[0]
    if nat_ip_fgt:
        nat_ip_pool_fgt.append(nat_ip_fgt[0])


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

# only_4g_fgt = ["FGTCE5001", "FGTEA5256", "FGTSH5132", "FGTEA5235", "FGTCE5141", "FGTWE5267", "FGTCE5151", "FGTNE5036",
#           "FGTEA5424L", "FGTCE5251", "FGTNE5034", "FGTGB5220", "FGTGB5042", "FGTNE5149", "FGTWE5153", "FGTGB5357L",
#           "FGTCE5583L", "FGTGB5194", "FGTGB5087", "FGTEA5032", "FGTGB5567L", "FGTEA5708L", "FGTCE5357L", "FGTSO5186",
#           "FGTSO5071", "FGTEA5182", "FGTGB5210", "FGTEA5300", "FGTCE5100", "FGTCE5395L", "FGTGB5034", "FGTWE5314L",
#           "FGTEA5291", "FGTEA5370L", "FGTCE5518L", "FGTGB5323", "FGTGB51019L", "FGTGB5425L", "FGTCE5027", "FGTEA5138",
#           "FGTGB5024", "FGTGB5258", "FGTGB5020", "FGTEA5106", "FGTGB5428L", "FGTGB5366L", "FGTGB5298", "FGTWE5450L",
#           "FGTWE5060", "FGTGB5337"]

only_4g_fgt = ["FGTCE5001", "FGTCE5141", "FGTCE5357L", "FGTCE5583L", "FGTEA5176", "FGTEA5182", "FGTEA5291",
               "FGTEA5370L", "FGTEA5424L", "FGTGB5020", "FGTGB5034", "FGTGB5042", "FGTGB5087", "FGTGB5220",
               "FGTGB5258", "FGTGB5298", "FGTGB5323", "FGTGB5428L", "FGTGB5567L", "FGTNE5149", "FGTSO5186",
               "FGTWE5032", "FGTWE5060", "FGTWE5153", "FGTWE5314L"]

now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time()))
fname = now + r"_fmg_report.csv"

with open(fname, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Status", "Reamrk"])
    for i in device_info_fmg:
        hostname = re.findall('.*"hostname":\s+"(FGT\w+)",\s+.*', i)
        conn_status = re.findall('.*"conn_status":\s+(\d),\s+.*', i)
        nat_ip_fmg = re.findall('.*"var06_nat_ip":\s+"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",\s+.*', i)
        # mgmt_if = re.findall('.*"mgmt_if":\s+"(wan|wwan)",\s+.*', i)
        if hostname:
            value_tun_ip = device_pool_fgt.get(nat_ip_fmg[0], 65535)
            if conn_status[0] == '1' and value_tun_ip == '101':
                writer.writerow([hostname[0], 'Good'])
            elif conn_status[0] == '1' and value_tun_ip == '102':
                if hostname[0] in only_4g_fgt:
                    writer.writerow([hostname[0], '4G', 'Only 4G'])
                else:
                    writer.writerow([hostname[0], '4G'])
            elif conn_status[0] == '1' and value_tun_ip == 65535:
                if nat_ip_fmg[0] in nat_ip_pool_fgt:
                    if hostname[0] in only_4g_fgt:
                        writer.writerow([hostname[0], 'Add tunnel IP!!!', 'Only 4G'])
                    else:
                        writer.writerow([hostname[0], 'Add tunnel IP!!!'])
                else:
                    if hostname[0] in only_4g_fgt:
                        writer.writerow([hostname[0], 'VPN Error!!!', 'Only 4G'])
                    else:
                        writer.writerow([hostname[0], 'VPN Error!!!'])
            elif conn_status[0] == '2' and nat_ip_fmg[0] in nat_ip_pool_fgt:
                writer.writerow([hostname[0], 'No Mgmt!!!'])
            elif conn_status[0] == '2':
                if hostname[0] in only_4g_fgt:
                    writer.writerow([hostname[0], 'Offline!', 'Only 4G'])
                else:
                    writer.writerow([hostname[0], 'Offline!'])
            else:
                writer.writerow([hostname[0], 'Null'])

# --------------------登出FMG--------------------

payload = "{\n\"id\":1,\n\"jsonrpc\":\"1.0\",\n\"method\":\"exec\",\n\"params\":[\n{\n\n\"url\":\"/sys/logout\"\n}\n],\n" \
          "\"session\": \"" + session_id[0] + "\",\n\"verbose\":1\n}"
headers = {}
requests.request("POST", url_fmg, headers=headers, data=payload, verify=False)

