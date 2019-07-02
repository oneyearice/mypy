#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧


import os
import re
import time

while True:
    x = os.popen('netstat -tulnp | grep 8[080]').read()
    ii = re.findall('8080|8000|80', x)
    if ii:

        print ('HTTP(TCP/UDP80xx)服务已打开')  # UDP的呢，显示不太友好，最好抓一下但是抓用到for，这就回到RE的方法1了
        break
    else:
        print('等待一秒重新开始监控')
        time.sleep(1)
        continue



if __name__ == '__main__':
    pass