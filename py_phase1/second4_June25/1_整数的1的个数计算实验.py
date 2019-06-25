#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧


def NumberOf1(n):
    # write code here
    return bin (n).replace ("0b", "").count ("1") if n >= 0 else bin (2 ** 32 + n).replace ("0b", "").count ("1")

a = 255
b = NumberOf1(a)

print(b)


if __name__ == '__main__':
    pass