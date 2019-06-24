#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧

import re

str = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

result = re.match('\s*(\d+)\s+([\dA-Fa-f]{4}\.[\dA-Fa-f]{4}\.[\dA-Fa-f]{4})\s+(\w+)\s+(\w+\d+/\d+/\d+)\s*',str).groups()



print('VLAN ID   :',result[0])
print('MAC       :',result[1])
print('Type      :',result[2])
print('Interface :',result[3])



if __name__ == '__main__':
    pass