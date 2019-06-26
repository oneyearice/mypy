#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧

l1 = [4,5,7,1,3,9,0]
l2 = l1.copy()
l2.sort()


# for i in range(0,7,1):
for i in range(len(l1)):
    print(l1[i],l2[i])


if __name__ == '__main__':
    pass