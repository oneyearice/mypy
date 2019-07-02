#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧


import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *
def Host(host):
    packet = IP(dst=host)/ICMP()
    result = sr1(packet, timeout=5, verbose=False)
    if result:
        x = host+''+'通'
        print(x,end='')
    else:
        x = host+' '+'不通!'
        print(x,end='')

Host('192.168.224.2')



if __name__ == '__main__':
    pass