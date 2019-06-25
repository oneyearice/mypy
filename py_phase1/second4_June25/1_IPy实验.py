#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧

#
from IPy import  IP
# testIP=IP('127.0.0.1').strBin()
# print (testIP)
# #
# # print(dir(IP))
# # # for i in testIP:
#     print(i)


ip = IP(IP('192.168.1.0').make_net('255.255.255.0'))
print(ip)
LL = []
for i in ip:
    LL.append(i)
print(LL[-2])

# print (IP('192.168.1.0').make_net('255.255.255.0'))
# print (IP('192.168.1.0/255.255.255.0',make_net=True))
# print (IP('192.168.1.0-192.168.1.255',make_net=True))
if __name__ == '__main__':
    pass