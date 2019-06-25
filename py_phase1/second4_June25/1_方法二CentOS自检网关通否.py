#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧


import os
import re

ifconfig_result = os.popen('ifconfig '+'ens33').read()

ip = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)  # 100%精确，谢谢~
mac = re.findall('[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}',ifconfig_result)

print(f'{"ipv4_add":10}:{ip[0]}')
print(f'{"netmask":10}:{ip[1]}')
print(f'{"broadcast":10}:{ip[2]}')
print(f'{"mac_addr":10}:{mac[0]}')


a = ip[0].split('.')
m = ip[1].split('.')
i = 0
l = []
while True:
    z = int(a[i]) & int(m[i])
    l.append(z)
    i += 1
    if i == 4:
        break

l[-1]=2
gw = f'{l[0]}.{l[1]}.{l[2]}.{l[3]}'

ping_result = os.popen('ping -c 3 '+gw).read()

result = re.findall('time=',ping_result)

print('CentOS是VMwareWorksation里的虚机，所以网关地址为:.2，因此网关IP地址为：' + gw)

if result:
    print('网关可达！')
else:
    print('网关不可达！')


if __name__ == '__main__':
    pass