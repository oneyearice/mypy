# #!/usr/bin/python3.7
# # -*- coding=utf-8 -*-
# #不知道这个是干嘛的，总之是linux里的bashell吧
#
from netmiko import ConnectHandler
import re

device_ct = {
    'host': '172.30.5.6',
    'username': 'cisco',
    'password': 'L1f@asa2017',
    'device_type': 'cisco_asa',
}

net_connect_ct = ConnectHandler(**device_ct)

cli = 'show conn | i flags'

result = net_connect_ct.send_command(cli)

x = re.split(r'[\n\r\n]',result)

# print(x[0])
# print(x[-2])
# print('最后一行'+ x[-1])

i = 0
tt = ()
while True:
    port = re.match('\s*\w+\s+\w+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:(\d+)'
                    '\s+\w+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:(\d+).*',x[i]).groups()  # port是个元组（outside_port，inside_port）
    i += 1
    tt += port

    # print(port)
    # print(tt)
    if x[i] == x[-1]:
        break
# print(tt)  # tt是个所有port相加，也就是说有的（outside_port，inside_port,outside_port，inside_port......）

ll = []
for s in tt:
    # print(s,tt.count(s))
    if tt.count(s) >= 30:
        # print(type(s))  # s 是字符串
        # print(type(tt)) # tt 是元组
        # print(type(tt.count(s)))  # tt.cout是整数
        # print(s,tt.count(s))
        ss = (s,tt.count(s))
        ll.append(ss)
        # ll = set(ll)
print(ll)

# set(ll)
print(set(ll))

#
# print(type(port))
# outside_port = port[0]
# inside_port = port[1]
# print(outside_port)
# print(inside_port)
#
# if outside_port in x[1]:
#     print(x[1])


if __name__ == '__main__':
    pass