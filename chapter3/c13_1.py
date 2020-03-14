import logging
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)
from kamene.all import *

class ping:
    def __init__(self, dstip):
        self.dstip = dstip
        self.srcip = None
        self.length = 64
    def src(self, srcip):
        self.srcip = srcip
    def size(self, length):
        self.length = length
    def ping1(self):
        ping_pkt = IP(dst=self.dstip, src=self.srcip)/ICMP()/('a'*self.length)
        ping_result = sr1(ping_pkt, timeout=2, verbose=False)
        if ping_result:
            print(self.dstip, 'Yes')
        else:
            print(self.dstip, 'No')
    def ping5(self):
        ping_pkt = IP(dst=self.dstip, src=self.srcip)/ICMP()/('a'*self.length)
        for i in range(5):
            ping_result = sr1(ping_pkt, timeout=2, verbose=False)
            if ping_result:
                print('!', end='', flush=True)
            else:
                print('.', end='', flush=True)



