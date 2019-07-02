#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧


import os
import re
import time



while True:

    x = os.popen('netstat -tulnp').read()

    l = x.strip().split('\n')

    for i in l:
        # y = re.findall('\s*(\w+)\s+\d+\s+\d+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)',i)  # 只能抓ipv4该方法去采纳了
        # y = re.findall('(([a-f0-9]{1,4}:){7}[a-f0-9]{1,4})', i)  # ipv6抓不出来,tmd太复杂了
        y = re.split('\s+',i)
        port = y[3].split(':')[-1]
        # print(y[0],port)
        ii = re.findall('8080|8000|80', port)
        # print(ii)
        if ii:  # if 'tcp' in y[0]这样就只看TCP了
            print('HTTP'+'('+y[0]+'/'+port+')'+'服务已经被打开')
            break  # 跳出本层循环，也就是for循环
    else:
        time.sleep(1)
        print('等待一秒重新开始监控')
        continue  # 继续whlie循环，不会走到下面的break


    break  # 跳出while循环



        # break
        # else:
        #     print('等待一秒重新开始监控')
        #     time.sleep(1)
        #     continue









if __name__ == '__main__':
    pass