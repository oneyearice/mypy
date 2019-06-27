#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧
import re


asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"
line = asa_conn.split('\n')


for i in range(len(line)):
    rr = re.match('\s*\w+\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):\s*(\d+)\s+\w+\s+'
             '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):\s*(\d+),\s+\w+\s+\d{1,2}:\d{1,2}:\d{1,2},\s+\w+\s+'
             '(\d+),\s+\w+\s+(\w+)\s*',line[i]).groups()
    # print(rr)
    print(f'{"src_ip":10}:{rr[0]:^20}|{"src_port":^12}:{rr[1]:^10}|{"dst_ip":10}:{rr[2]:^20}|{"dst_port":^12}:{rr[3]:^10}'
          f'\n{"bytes":10}:{rr[4]:^20}|{"flags":^12}:{rr[5]:^10}'
          f'\n{"="*118}')





if __name__ == '__main__':
    pass