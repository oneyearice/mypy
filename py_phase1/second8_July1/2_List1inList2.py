#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧

list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

for x in list1:  # 取出list1的第一个字符

    if x in list2:
        print(x,'both in list1 and list2')
    else:
        print(x,'only in list1')



if __name__ == '__main__':
    pass