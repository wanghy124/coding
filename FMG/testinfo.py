import re
# import os
# import time
# #
# D1 = b'{ "id": 1, "result": [ { "data": [ { "adm_pass": [ "ENC", "X2KSSN0iZCkK6j1XEvwxMQFH5rlzLAaGQSNxrX1i5qzRw7PtqTmz5Jkx29mJkG91XV794SaWnAGojY+ahnvV8a1y8Xa5rBtPJYc7iYQN33xpSRt83iTgiDLvpl+W1st3Tp4Vurscwbv3fjwtVeLEZVJcwweDJ4gpNc901r7A7zUGAc0b" ], "adm_usr": "admin", "app_ver": "", "av_ver": "1.00000(2018-04-09 18:07)", "beta": -1, "branch_pt": 1010, "build": 1010, "checksum": "12 b5 30 23 8f 7d 06 c4 40 f9 ae d1 a1 e7 2e 2a", "conf_status": 2, "conn_mode": 1, "conn_status": 1, "db_status": 1, "desc": "", "dev_status": 15, "fap_cnt": 0, "faz.full_act": 0, "faz.perm": 15, "faz.quota": 0, "faz.used": 0, "fex_cnt": 0, "flags": 4194560, "foslic_cpu": 0, "foslic_dr_site": 0, "foslic_inst_time": 0, "foslic_last_sync": 0, "foslic_ram": 0, "foslic_type": 0, "foslic_utm": 0, "fsw_cnt": 0, "ha_group_id": 0, "ha_group_name": "", "ha_mode": 0, "ha_slave": null, "hdisk_size": 0, "hostname": "FGTCE5001", "hw_rev_major": 17460, "hw_rev_minor": 5, "ip": "36.155.93.198", "ips_ext": 0, "ips_ver": "6.00741(2015-12-01 02:30)", "last_checked": 1576326899, "last_resync": 1572947196, "latitude": "0.0", "lic_flags": 0, "lic_region": "", "location_from": "diag", "logdisk_size": 0, "longitude": "0.0", "maxvdom": 5, "meta fields": { "Address": "\xe9\x99\x95\xe8\xa5\xbf\xe7\x9c\x81\xe8\xa5\xbf\xe5\xae\x89\xe5\xb8\x82\xe6\x96\xb0\xe5\x9f\x8e\xe5\x8c\xba\xe8\xa7\xa3\xe6\x94\xbe\xe8\xb7\xaf103\xe5\x8f\xb7\xe6\xac\xa7\xe8\x8e\xb1\xe9\x9b\x85\xe6\x9f\x9c\xe5\x8f\xb0", "Contact": "\xe6\x9d\xa8\xe7\x91\x9e", "Contact Phone Number": "18629350633", "Store Name": "\xe8\xa5\xbf\xe5\xae\x89\xe6\xb0\x91\xe7\x94\x9f-\xe4\xb8\x93\xe6\x9f\x9cL", "var01_hostname": "FGTCE5001", "var02_internal_gateway_ip": "10.32.218.254", "var03_dhcp_start_ip": "10.32.218.50", "var04_dhcp_end_ip": "10.32.218.200", "var05_local_subnet": "10.32.218.0", "var06_nat_ip": "10.162.144.218", "var07_pppoe_username": "", "var08_pppoe_password": "", "var09_max_bw_kbps": "", "var10_guarantee_bw_kbps": "" }, "mgmt.__data[0]": 2690466, "mgmt.__data[1]": 0, "mgmt.__data[2]": 0, "mgmt.__data[3]": 0, "mgmt.__data[4]": 1054822400, "mgmt.__data[5]": 0, "mgmt.__data[6]": 1, "mgmt.__data[7]": 0, "mgmt_id": 604330058, "mgmt_if": "wwan", "mgmt_mode": 3, "mgt_vdom": "root", "module_sn": "", "mr": 2, "name": "FGTCE5001", "node_flags": 0, "oid": 1137, "opts": 0, "os_type": 0, "os_ver": 6, "patch": 2, "platform_str": "FortiWiFi-30E", "prefer_img_ver": "", "psk": "", "sn": "FWF30E5619007126", "source": 1, "tab_status": "[ \\"KW_inherit\\", \\"dashboard\\", \\"interface\\", \\"ha\\", \\"snmp\\", \\"replacemsg\\", \\"staticroute_all\\", \\"ospf\\", \\"phase1_all\\", \\"phase2_all\\", \\"queryvpn\\" ]", "tunnel_cookie": "", "tunnel_ip": "", "vdom": [ { "comments": null, "devid": "FGTCE5001", "ext_flags": 1, "flags": 1, "name": "root", "node_flags": 0, "oid": 3, "opmode": 1, "rtm_prof_id": 0, "status": null, "tab_status": null, "vpn_id": 0 } ], "version": 600, "vm_cpu": 2, "vm_cpu_limit": 0, "vm_lic_expire": 0, "vm_mem": 1005, "vm_mem_limit": 0, "vm_status": 0 }, { "adm_pass": [ "ENC", "Z22ELX2sU3I0W0GH3OUbOKLTEM+O4eZ5i\\/4bDWO2mzQ+TB1Il1Xi5oONqSA9P+kZ\\/cnKUKd1NFqLB9CiMqchSwpQGr13HHtBjQ8oJg4WT8Xru4zrBZWVrWd5yNf1qOSnMwQy2r3spdkevyyECeqYUJuk2g2IaEbh8\\/4l9DXcxM4nTWWn" ], "adm_usr": "admin", "app_ver": "", "av_ver": "1.00000(2018-04-09 18:07)", "beta": -1, "branch_pt": 1010, "build": 1010, "checksum": "8a e7 d0 04 55 e1 ee d3 09 c8 0b 8b 02 b9 fb 67", "conf_status": 1, "conn_mode": 1, "conn_status": 2, "db_status": 1, "desc": "", "dev_status": 15, "fap_cnt": 0, "faz.full_act": 0, "faz.perm": 15, "faz.quota": 0, "faz.used": 0, "fex_cnt": 0, "flags": 4194560, "foslic_cpu": 0, "foslic_dr_site": 0, "foslic_inst_time": 0, "foslic_last_sync": 0, "foslic_ram": 0, "foslic_type": 0, "foslic_utm": 0, "fsw_cnt": 0, "ha_group_id": 0, "ha_group_name": "", "ha_mode": 0, "ha_slave": null, "hdisk_size": 0, "hostname": "FGTCE5002", "hw_rev_major": 17460, "hw_rev_minor": 5, "ip": "36.155.93.197", "ips_ext": 0, "ips_ver": "6.00741(2015-12-01 02:30)", "last_checked": 1574085864, "last_resync": 1573723039, "latitude": "31.491171", "lic_flags": 0, "lic_region": "", "location_from": "unset", "logdisk_size": 0, "longitude": "120.311913", "maxvdom": 5, "meta fields": { "Address": "\xe9\x99\x95\xe8\xa5\xbf\xe7\x9c\x81\xe8\xa5\xbf\xe5\xae\x89\xe5\xb8\x82\xe4\xb8\x9c\xe5\xa4\xa7\xe8\xa1\x97\xe8\xa7\xa3\xe6\x94\xbe\xe5\xb8\x82\xe5\x9c\xba6\xe5\x8f\xb7\xe6\xac\xa7\xe8\x8e\xb1\xe9\x9b\x85\xe6\x9f\x9c\xe5\x8f\xb0", "Contact": "\xe6\x9d\xa8\xe7\x91\x9e", "Contact Phone Number": "18629350633", "Store Name": "\xe8\xa5\xbf\xe5\xae\x89\xe5\xbc\x80\xe5\x85\x83-\xe4\xb8\x93\xe6\x9f\x9cL", "var01_hostname": "FGTCE5002", "var02_internal_gateway_ip": "10.32.217.254", "var03_dhcp_start_ip": "10.32.217.50", "var04_dhcp_end_ip": "10.32.217.200", "var05_local_subnet": "10.32.217.0", "var06_nat_ip": "10.162.144.217", "var07_pppoe_username": "029007615916", "var08_pppoe_password": "093nme", "var09_max_bw_kbps": "", "var10_guarantee_bw_kbps": "" }, "mgmt.__data[0]": 2690466, "mgmt.__data[1]": 0, "mgmt.__data[2]": 0, "mgmt.__data[3]": 0, "mgmt.__data[4]": 1054822400, "mgmt.__data[5]": 0, "mgmt.__data[6]": 1, "mgmt.__data[7]": 0, "mgmt_id": 76081199, "mgmt_if": "wwan", "mgmt_mode": 3, "mgt_vdom": "root", "module_sn": "", "mr": 2, "name": "FGTCE5002", "node_flags": 0, "oid": 2800, "opts": 0, "os_type": 0, "os_ver": 6, "patch": 2, "platform_str": "FortiWiFi-30E", "prefer_img_ver": "", "psk": "", "sn": "FWF30E5619010095", "source": 1, "tab_status": "", "tunnel_cookie": "", "tunnel_ip": "", "vdom": [ { "comments": null, "devid": "FGTCE5002", "ext_flags": 1, "flags": 1, "name": "root", "node_flags": 0, "oid": 3, "opmode": 1, "rtm_prof_id": 0, "status": null, "tab_status": null, "vpn_id": 0 } ], "version": 600, "vm_cpu": 2, "vm_cpu_limit": 0, "vm_lic_expire": 0, "vm_mem": 1005, "vm_mem_limit": 0, "vm_status": 0 } ], "status": { "code": 0, "message": "OK" }, "url": "\\/dvmdb\\/device" } ] }'
#
# D = D1.decode().split('adm_pass')
# # print(D[1])
#
# list1 = [['10.162.144.218','36.155.93.199'],['10.162.144.217','36.155.93.196']]
#
# for i in D:
#     hostname = re.findall('.*"hostname":\s+"(\w+\d+)",\s+.*', i)
#     conn_status = re.findall('.*"conn_status":\s+(\d),\s+.*', i)
#     mgmt_if = re.findall('.*"mgmt_if":\s+"(wan|wwan)",\s+.*', i)
#     if hostname:
#         if conn_status[0] == '1' and mgmt_if[0] == 'wan':
#             print('%s 正常'% hostname[0])
#         elif conn_status[0] == '1' and mgmt_if[0] == 'wwan':
#             mgmt_ip = re.findall('.*"ip":\s+"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",\s+.*', i)
#             nat_ip = re.findall('.*"var06_nat_ip":\s+"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",\s+.*', i)
#             if [nat_ip[0],mgmt_ip[0]] in list1:
#                 print('%s 4G'% hostname[0])
#             else:
#                 print('%s 正常' % hostname[0])
#         elif conn_status[0] == '2':
#             print('%s 离线'% hostname[0])
#         else:
#             print('Null')
#
#
#
# # now = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time()))
# # fname = now + r"_fmg_report.csv"
# # file = open(fname,'w')
# # file.write('中文\n'.encode("utf-8"))
# # file.close()


a = '''/home/rconfig/data/CiscoRouters/RCS-20F-Router1/2021/Mar/08/showstartup-config-1738.txt
/home/rconfig/data/CiscoFirewalls/BJLFS-FW/2021/Mar/08/showstartup-config-1738.txt
/home/rconfig/data/CiscoFirewalls/BJLFS-FW/2021/Mar/08/showstartup-config-1751.txt
/home/rconfig/data/CiscoSwitches/RCS-20F-SW1/2021/Mar/08/showstartup-config-1738.txt
/home/rconfig/data/CiscoSwitches/ASCSZSW3750XS01/2021/Mar/08/showstartup-config-1641.txt
/home/rconfig/data/CiscoSwitches/ASCSZSW3750XS01/2021/Mar/08/showstartup-config-1717.txt
/home/rconfig/data/CiscoSwitches/ASCSZSW3750XS01/2021/Mar/08/showstartup-config-1731.txt
/home/rconfig/data/CiscoSwitches/RCS-20F-CORE1/2021/Mar/08/showstartup-config-1738.txt
/home/rconfig/data/CiscoSwitches/RCS-20F-CORE1/2021/Mar/08/showstartup-config-1704.txt
/home/rconfig/data/CiscoSwitches/RCS-20F-SW9/2021/Mar/08/showstartup-config-1738.txt'''

file_list = str(a).split('\n')
a=0
for i in file_list:
    if a < len(file_list)-1:
        if re.match('/home/rconfig/data/\w+/([-\w]+)/.*', i) == re.match('(CN[-A-Za-z0-9]*)\s+', file_list[a + 1]):
            continue
        else:


