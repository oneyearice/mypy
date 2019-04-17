# import random
#
# seg1 = random.randint(1,255)
# seg2 = random.randint(1,255)
# seg3 = random.randint(1,255)
# seg4= random.randint(1,255)
# random_ip = str(seg1) + '.' + str(seg2) + '.' + str(seg3) + '.' + str(seg4)
#
# print(random_ip)
#
# x = 'hello'
# X = x.upper()
# print(X)
#

import re
import os
ifconfig_result = os.popen('ifconfig '+'ens33').read()
re_findall_result = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)
print(type(re_findall_result))
print(re_findall_result)
for x in re_findall_result:
    print(x)
    print(type(x))
    print(x.split('.'))
    print(type(x.split('.')))

print(re_findall_result[1])
print(re_findall_result[1][-1:])

for ip in re_findall_result:
    if ip.split('.')[-1] == '0':
        mask = ip
        # print(mask)
    elif ip.split('.')[-1] == '255':
        broadcast = ip
        # print(broadcast)
    else:
        ipv4_ip = ip
        # print(ipv4_ip)


# print('NetMask:'+ mask)
print('{0:<12}|{1:^22}'.format('Netmask:',mask))
print('{0:<12}|{1:^22}'.format('Broadcast:',broadcast))
print('{0:<12}|{1:^22}'.format('ipv4:',ipv4_ip))
# print('Broad:'+ broadcast)
# print('IPv4:'+ ipv4_ip)
