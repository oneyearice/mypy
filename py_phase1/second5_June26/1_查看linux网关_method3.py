#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧

import os
import re


route_n_result = os.popen('route -n').read()

line = route_n_result.split('\n')

l = re.split('\s+',line[2])


print('网关为:'+l[1])


if __name__ == '__main__':
    pass