#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧

import re

str = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

result = re.match('(\w+)\s+(\w+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+)\s+'
                  '(\w+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+)\s*,\s+(\w+)\s+'
                  '(\d{1,2}:\d{1,2}:\d{1,2})\s*,\s+(\w+)\s+(\d+)\s*,\s+(\w+)\s+(\w+)\s*',str).groups()

# print(type(result))
# print(result[6].split(':'))
ll = result[6].split(':')  # 将xx:xx:xx换成xx小时xx分钟xx秒
tt = ll[0]+'小时'+ll[1]+'分钟'+ll[2]+'秒'  # 将xx:xx:xx换成xx小时xx分钟xx秒
result = list(result)  # 将 该result元组 转成列表 才能修改
result[6] = tt  #修改时间格式为tt格式
# print(tt)

print(f'{"protocol":17}: {result[0]}')
i = 1
while True:

    print(f'{result[i]:17}: {result[i + 1]:10}')

    if result[i+1] == result[-1]:  # 如果到达列表最后一个元素，则跳出while循环
        break

    i += 2


if __name__ == '__main__':
    pass