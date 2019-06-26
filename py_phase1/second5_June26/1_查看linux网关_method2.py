#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧

import os
import re


route_n_result = os.popen('route -n').read()

gw = re.findall('0\.0\.0\.0\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+0\.0\.0\.0',route_n_result)

print(gw)
print('网关为:'+gw[0])

if __name__ == '__main__':
    pass