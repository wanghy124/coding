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

ld_fgt = ["FGTUT0", "FGTH20", "FGTAT0", "FGT780", "FGT0A0", "FGT0D0", "FGTA90", "FGTKA0", "FGTVO0", "FGTMI0",
           "FGTRK0", "FGTRO0", "FGT1V0", "FGTS70", "FGTG70", "FGTII0", "FGT8R0", "FGTP70", "FGT0F0", "FGTSP0",
           "FGTI30", "FGT2Q0", "FGT2R0", "FGTI00", "FGT3P0", "FGTA10", "FGT4W0", "FGT690", "FGTGL0", "FGT380",
           "FGTIE0", "FGTCT0", "FGTRH0", "FGT4L0", "FGTAH0", "FGT2A0", "FGTSQ0", "FGTK50", "FGTMB0", "FGT3Y0",
           "FGT7G0", "FGT8Q0", "FGT5A0", "FGT060", "FGTKZ0", "FGT1O0", "FGTHA0", "FGTAB0", "FGTVQ0", "FGT4Q0",
           "FGTYC0", "FGTKV0", "FGTKT0", "FGTY20", "FGTK40", "FGTBQ0", "FGT3X0", "FGTBP0", "FGTIZ0", "FGTGA0",
           "FGT1P0", "FGTJ20", "FGT9D0", "FGT320", "FGTI50", "FGTUT0SHU", "FGT3L0", "FGTWE0", "FGTRP0", "FGTAD0",
           "FGT3I0", "FGTS50", "FGTBC0", "FGTCJ0", "FGTY60", "FGTBJ0", "FGTYJ0", "FGTOO0", "FGTYQ0", "FGTOM0",
           "FGTOT0", "FGTBW0", "FGTC60", "FGTE20", "FGT040", "FGTHN0", "FGT080", "FGTRD0", "FGTM90", "FGT3N0",
           "FGTSL0", "FGTG90", "FGTP50", "FGTIR0", "FGT3H0", "FGT3M0", "FGTBH5", "FGTCU0", "FGT120", "FGT2J0",
           "FGT020", "FGTH10", "FGTWL0", "FGTAI0", "FGTRF0", "FGTBS0", "FGT8V0", "FGTIA0", "FGTS30", "FGTSI0",
           "FGTG40", "FGTA65", "FGT7I0", "FGTID0", "FGT2C0", "FGTSD0", "FGTAZ0", "FGT760", "FGT260", "FGT3Q0",
           "FGTS40", "FGTP90", "FGT5B0", "FGTOL0", "FGTUW0", "FGTAM0", "FGTJ50", "FGTJ00", "FGTSN0", "FGT2N0",
           "FGTC80", "FGT2D0", "FGT200", "FGT210", "FGT7F0", "FGTKW0", "FGTH70", "FGTH60", "FGT300", "FGTSE0",
           "FGTIF0", "FGTOE0", "FGTGJ0", "FGT7H0", "FGT0G0", "FGTSW0", "FGTB50", "FGTYK0", "FGTA30", "FGTK10",
           "FGTCL0", "FGTJG0", "FGT1U0", "FGTSM0", "FGTAQ0", "FGT0Q0", "FGTI10", "FGTY90", "FGTTD0", "FGTLE0",
           "FGTO50", "FGTLI0", "FGTB20", "FGTB70", "FGTK60", "FGTY30", "FGTBX0", "FGTYN0", "FGTFF0", "FGTAU5",
           "FGTAC5", "FGTG80", "FGT6D0", "FGTAH5", "FGTEG0", "FGTKI0", "FGT1Y0", "FGTVD0", "FGTGO0", "FGTIV0",
           "FGTIP0", "FGTVT0", "FGT7X0", "FGTDO0", "FGTUN0", "FGT4P0", "FGTAV0", "FGTBZ0", "FGT9L0", "FGT0V0",
           "FGTIW0", "FGTG60", "FGT4Z0", "FGTUP0", "FGT8B0", "FGT2Y0", "FGTMO0", "FGTFK0", "FGTEM5", "FGT7R0",
           "FGTVC0", "FGTW50", "FGT1B0", "FGTG50", "FGT2G0", "FGTU40", "FGT400", "FGTD10", "FGT350", "FGTGP0",
           "FGTYT0", "FGTD70", "FGTKO0", "FGTYX0", "FGT5R0", "FGTG10", "FGT680", "FGT550", "FGTRC0", "FGTYI0",
           "FGTC20", "FGTKD0", "FGTE90", "FGT1H0", "FGT3F0", "FGTM60", "FGT1A0", "FGT0B0", "FGTRR0", "FGTGS0",
           "FGTS20", "FGTLC0", "FGTOH0", "FGTYF0", "FGTC40", "FGTKG0", "FGT1G0", "FGTSK0", "FGTHS0", "FGTJN0",
           "FGTJ90", "FGTCO0", "FGTGG0", "FGT0I0", "FGTBG0", "FGTYG0", "FGTYV0", "FGTBF0", "FGTY70", "FGTBH0",
           "FGTK80", "FGTYA0", "FGTW70", "FGT0W0", "FGTOA0", "FGTYD0", "FGTCW0", "FGTW00", "FGTBB0", "FGT130",
           "FGTBA0", "FGTKC0", "FGT1J0", "FGTHE0", "FGTA50", "FGTD40", "FGT2L0", "FGTLD0", "FGTKL0", "FGT7Y0",
           "FGT5V0", "FGTYH0", "FGTEP0", "FGTCG0", "FGTTP0", "FGTJS0", "FGTHF0", "FGTAP0", "FGTJA0", "FGTSS0",
           "FGT150", "FGTH50", "FGT2S0", "FGTKS0", "FGTB80", "FGTB90", "FGTKU0", "FGTYU0", "FGT6G0", "FGTUS0",
           "FGT9R0", "FGT9Q0", "FGTSX0", "FGT170", "FGTKY0", "FGTVP0", "FGTA60", "FGT8E0", "FGT8U0", "FGT2V0"]

#CPD
now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time()))
fname = now + r"_fmg_cpd_report.csv"

with open(fname, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Status", "Reamrk"])
    for i in device_info_fmg:
        hostname = re.findall('.*"hostname":\s+"(FGT\w+)",\s+.*', i)
        conn_status = re.findall('.*"conn_status":\s+(\d),\s+.*', i)
        nat_ip_fmg = re.findall('.*"var06_nat_ip":\s+"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",\s+.*', i)
        # mgmt_if = re.findall('.*"mgmt_if":\s+"(wan|wwan)",\s+.*', i)
        if hostname:
            if hostname[0] not in ld_fgt:
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


#LD
now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time()))
fname = now + r"_fmg_ld_report.csv"

with open(fname, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Status", "Reamrk"])
    for i in device_info_fmg:
        hostname = re.findall('.*"hostname":\s+"(FGT\w+)",\s+.*', i)
        conn_status = re.findall('.*"conn_status":\s+(\d),\s+.*', i)
        nat_ip_fmg = re.findall('.*"var06_nat_ip":\s+"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",\s+.*', i)
        # mgmt_if = re.findall('.*"mgmt_if":\s+"(wan|wwan)",\s+.*', i)
        if hostname:
            if hostname[0] in ld_fgt:
                value_tun_ip2 = device_pool_fgt.get(nat_ip_fmg[0], 65535)
                if conn_status[0] == '1' and value_tun_ip2 == '101':
                    writer.writerow([hostname[0], 'Good'])
                elif conn_status[0] == '1' and value_tun_ip2 == '102':
                    if hostname[0] in only_4g_fgt:
                        writer.writerow([hostname[0], '4G', 'Only 4G'])
                    else:
                        writer.writerow([hostname[0], '4G'])
                elif conn_status[0] == '1' and value_tun_ip2 == 65535:
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

