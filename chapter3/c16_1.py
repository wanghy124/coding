import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *
import ipaddress
from multiprocessing import Pool as Processpool
from multiprocessing.pool import ThreadPool
from multiprocessing import freeze_support
import pickle
import datetime

def ping_scan(dst_ip):
    ping_pkt = IP(dst=dst_ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return dst_ip, 1
    else:
        return dst_ip, 2

if __name__ == '__main__':
    freeze_support()
    pool = ThreadPool(processes=150)
    result = []
    net = ipaddress.ip_network('192.168.27.0/29')
    for ip in net.hosts():
        result.append(pool.apply_async(ping_scan, args=(str(ip),)))
        # print(result[0])
    pool.close()
    pool.join()
    active_host = []
    for i in result:
        if i.get()[1] == 1:
            active_host.append(i.get()[0])
    print(active_host)

    now = datetime.datetime.now()
    fname = 'scan_save_pickle_' + now.strftime('%Y-%m-%d_%H-%M-%S') + '.pl'
    with open(fname, 'wb') as f:
        pickle.dump(active_host, f)

    f = open(fname, 'rb')
    print(pickle.load(f))






