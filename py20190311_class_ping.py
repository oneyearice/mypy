import logging
logging.getLogger('kamene,runtime').setLevel(logging.ERROR)
from kamene.all import *

class Qytang:
    def __init__(self,ip):
        self.ip = ip
        self.srcip = None
        self.length = 100
        self.pkt = IP(dst=self.ip,src=self.srcip) / ICMP() / (b'v' * self.length)

    def src(self,srcip):
        self.srcip = srcip
        self.pkt = IP(dst=self.ip,src=self.srcip) / ICMP() / (b'v' * self.length)

    def size(self,length):
        self.length = length
        self.pkt = IP(dst=self.ip,src=self.srcip) / ICMP() / (b'v' * self.length)

    def one(self):
        result = sr1(self.pkt,timeout=1,verbose=False)
        if result:
            print(self.ip,'可达')
        else:
            print(self.ip,'不可达')

    def ping(self):
        for i in range(5):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print('!',end='')
            else:
                print('.',end='')
        print()


    def __str__(self):
        return "<srcip:%s,dstip:%s,size:%s>"% (self.srcip,self.ip,self.length)



class Newping(Qytang):
    def ping(self):
        # Qytang.ping(self)
            for i in range(5):
                result = sr1(self.pkt, timeout=1, verbose=False)
                if result:
                    print('+',end='')
                else:
                    print('?',end='')
            print()
