#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from argparse import ArgumentParser
import paramiko
import re

def paramiko_ssh(IPADDR, USERNAME, PASSWORD, COMMAND, port=22):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(IPADDR, port=port, username=USERNAME, password=PASSWORD, timeout=5, compress=True)
        stdin, stdout, stderr = ssh.exec_command(COMMAND)
        x = stdout.read().decode()
        return x
    except Exception as e:
        if re.match('.*Authentication failed.*', str(e)):
            print(f'{IPADDR} 连接失败！{e}')


if __name__ == '__main__':
    usage = 'python Simple_SSH_Client IPADDR -u USERNAME -p PASSWORD -c COMMAND'

    parser = ArgumentParser(usage=usage)
    parser.add_argument(nargs='?', dest='IPADDR', help='SSH Server', default='1.1.1.1', type=str)
    parser.add_argument('-u', '--username', dest='USERNAME', help='SSH Username', default='root', type=str)
    parser.add_argument('-p', '--password', dest='PASSWORD', help='SSH Password', default='cisco', type=str)
    parser.add_argument('-c', '--command', dest='COMMAND', help='Shell Command', default='ls', type=str)
    args = parser.parse_args()

    print(paramiko_ssh(args.IPADDR, args.USERNAME, args.PASSWORD, args.COMMAND))







