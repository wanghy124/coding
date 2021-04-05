import paramiko
import time
import os
import re

def ssh_tool(ip, username, password, verbose=True):
    ssh = paramiko.SSHClient()  # 创建SSH Client
    ssh.load_system_host_keys()  # 加载系统SSH密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加新的SSH密钥
    ssh.connect(ip, port=22, username=username, password=password, timeout=10, compress=True, allow_agent=False,
                look_for_keys=False)  # SSH连接

    chan = ssh.invoke_shell()  # 激活交互式shell
    time.sleep(1)

    ap_list = []

    chan.send(username)
    chan.send(b'\n')
    chan.send(password)
    chan.send(b'\n')
    time.sleep(3)
    chan.send(b'sudo -i')
    chan.send(b'\n')
    time.sleep(1)
    chan.send(b'find /home/rconfig/data -name "showstartup-config*.txt"')
    chan.send(b'\n')
    time.sleep(3)
    output = chan.recv(200000).decode()  # 读取回显，有些回想可能过长，请把接收缓存调大
    if verbose:
        print(output)  # 打印回显

    file_list = str(output).split('\n')
    for i in file_list:
        hostname = re.match('(CN[-A-Za-z0-9]*)\s+', i)
        if hostname:
            ap_list.append(ap[0])