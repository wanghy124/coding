#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from argparse import ArgumentParser
import paramiko

def paramiko_ssh(IPADDR, USERNAME, PASSWORD, COMMAND, port=22):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IPADDR, port=port, username=USERNAME, password=PASSWORD, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(COMMAND)
    x = stdout.read().decode()
    return x

if __name__ == '__main__':
    usage = 'python Simple_SSH_Client -i ipaddr -u username -p password -c command'

    parser = ArgumentParser(usage=usage)
    parser.add_argument(nargs='?', dest='IPADDR', help='SSH Server', default='1.1.1.1', type=str)
    parser.add_argument('-u', '--username', dest='USERNAME', help='SSH Username', default='root', type=str)
    parser.add_argument('-p', '--password', dest='PASSWORD', help='SSH Password', default='cisco', type=str)
    parser.add_argument('-c', '--command', dest='COMMAND', help='Shell Command', default='ls', type=str)
    args = parser.parse_args()

    paramiko_ssh(args.IPADDR, args.USERNAME, args.PASSWORD, args.COMMAND)

