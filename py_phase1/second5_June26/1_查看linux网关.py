#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧

import os
import re
route_n_result = os.popen('route -n').read()

line = route_n_result.split('\n')

gw = re.match('0\.0\.0\.0\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+0\.0\.0\.0\s+UG\s+.*',line[2]).groups()
print(gw)
print('网关为:'+gw[0])

if __name__ == '__main__':
    pass



print(test)