#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧

import re
from IPy import IP
from netmiko import ConnectHandler



device = {
    'host':'192.168.224.159',
    'username':'root',
    'password':'Cisc0@123',
    'device_type':'linux'
}

connect = ConnectHandler(**device)
cli_1 = 'ifconfig ens33'
result_1 = connect.send_command(cli_1)
# print(result)
ip = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',result_1)
mac = re.findall('[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}',result_1)


add = IP(ip[0]).int()
mask = IP(ip[1]).int()
sub = add & mask
ip_sub = IP(IP(sub)).make_net(IP(mask))

LL = []
for i in ip_sub:
    LL.append(i)
gw = str(LL[2])
# print(gw)

cli_2 = 'ping -c 3 ' + gw
# print(cli_2)
result_2 = connect.send_command(cli_2)
result = re.findall('time=',result_2)
# print(result)

print(f'{"ipv4_add":10}:{ip[0]}')
print(f'{"netmask":10}:{ip[1]}')
print(f'{"broadcast":10}:{ip[2]}')
print(f'{"mac_addr":10}:{mac[0]}')

print('CentOS是VMwareWorksation里的虚机，所以网关地址为:.2，因此网关IP地址为：' + gw)

if result:
    print('网关可达！')
else:
    print('网关不可达！')

if __name__ == '__main__':
    pass