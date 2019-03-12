import re
import os
data = os.popen('ifconfig '+'ens33').read()
# words = data.split()
# print(data)
# print(words)
re_find_result = re.findall('\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}',data)

# print(re_find_result)
for ip in re_find_result:
    if ip.split('.')[-1] == '0':
        mask = ip
    elif ip.split('.')[-1] == '255':
        bradcast = ip
    else:
        ipv4_ip = ip
print('{}{}'.format('ipv4 addr:',ipv4_ip))
print('{}{}'.format('mask:',mask))
print('{}{}'.format('broadcast :',bradcast))
