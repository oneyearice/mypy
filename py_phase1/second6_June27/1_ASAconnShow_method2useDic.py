#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧



import re


asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

asa_dict = {}

for i in asa_conn.split('\n'):
    rr = re.match('\s*\w+\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):\s*(\d+)\s+\w+\s+'
             '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):\s*(\d+),\s+\w+\s+\d{1,2}:\d{1,2}:\d{1,2},\s+\w+\s+'
             '(\d+),\s+\w+\s+(\w+)\s*',i).groups()
    asa_dict[rr[0:4]] = (rr[4:])

print('打印分析后的字典！注意字典在列表中\n\n',asa_dict)


print('\n格式化打印输出\n')

for key, value in asa_dict.items():
    print(f'{"src_ip":^10}:{key[0]:^20}|{"src_port":^12}:{key[1]:^10}|{"dst_ip":^10}:{key[2]:^20}|{"dst_port":^12}:{key[3]:^10}'
              f'\n{"bytes":^10}:{value[0]:^20}|{"flags":^12}:{value[1]:^10}'
              f'\n{"="*118}')


if __name__ == '__main__':
    pass