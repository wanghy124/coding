

import os
import paramiko
import time
import re
# def ssh_tool(ip, username, password, verbose=True):
#     try:
#         ssh = paramiko.SSHClient()  # 创建SSH Client
#         ssh.load_system_host_keys()  # 加载系统SSH密钥
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加新的SSH密钥
#         ssh.connect(ip, port=22, username=username, password=password, timeout=10, compress=True, allow_agent=False,
#                     look_for_keys=False)  # SSH连接
#
#         chan = ssh.invoke_shell()  # 激活交互式shell
#         time.sleep(1)
#
#         chan.send(username)
#         chan.send(b'\n')
#         chan.send(password)
#         chan.send(b'\n')
#         time.sleep(3)
#         chan.send(b'show ap summary')
#         chan.send(b'\n')
#         time.sleep(3)
#         output = chan.recv(200000).decode()  # 读取回显，有些回显可能过长，请把接收缓存调大
#         if verbose:
#             print(output)  # 打印回显
#
#         chan.close()  # 退出交互式shell
#         ssh.close()  # 退出ssh会话
#
#     except Exception as e:
#         fname = r"Error_" + ip + r".txt"
#         with open(fname, "w", newline='') as file:
#             file.write(ip + '\n')
#             file.write(str(e))
#
# if __name__ == '__main__':
#     ssh_tool('1.1.1.1', 'admin', 'admin')
#     os.system('pause')


text ='Attributes for Slot  0 Radio Type................................... RADIO_TYPE_80211n-2.4 Administrative State ........................ ADMIN_DISABLED Operation State ............................. DOWN Operation State Down Cause................... Radio reset due to (123) Radio Admin State Change'

radio = re.findall('.*RADIO_TYPE_80211n-2.4\s+Administrative State \.+\s(ADMIN_DISABLED|ADMIN_ENABLED).*', text)

print(radio)