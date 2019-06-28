#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧
import re

port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34'
    ,'eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']

# port_list.sort(key=lambda x: (int(re.match('\w+\s+(\d+)/(\d+)/(\d+)/(\d+)',x).groups()[0]),
# int(re.match('\w+\s+(\d+)/(\d+)/(\d+)/(\d+)',x).groups()[1]),
# int(re.match('\w+\s+(\d+)/(\d+)/(\d+)/(\d+)',x).groups()[2]),
# int(re.match('\w+\s+(\d+)/(\d+)/(\d+)/(\d+)',x).groups()[3])
#                               )

port_list.sort(key=lambda x: (int(re.findall('\d+', x)[0]),
                              int(re.findall('\d+', x)[1]),
                              int(re.findall('\d+', x)[2]),
                              int(re.findall('\d+', x)[3])
                              )
               )

print(port_list)


if __name__ == '__main__':
    pass