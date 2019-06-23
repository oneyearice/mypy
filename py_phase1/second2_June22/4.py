#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
#不知道这个是干嘛的，总之是linux里的bashell吧


department1 = 'AVdEveLopMenT'
department2 = 'ManAttachment'
depart1_m = 'xiaohei'
depart2_m = 'Amu'
COUSE_FEES_AV = 733817.212313
COUSE_FEES_Man = 12321.23212


line1 = "department1 name:%-16sManger:%-10sCOUSE_FEES  %-12.2fthe end!" % (department1,depart1_m,COUSE_FEES_AV)
line2 = "department2 name:%-16sManger:%-10sCOUSE_FEES  %-12.2fthe end!" % (department2,depart2_m,COUSE_FEES_Man)
length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)


line1 = '{0}{1:16}Manger:{2:10}COUSE_FEES  {3:<12.2f}the end!'\
    .format('department1 name:',department1,depart1_m,COUSE_FEES_AV)  # 这一行与众不同，多了一个固定的字符串，也没啥其实
line2 = 'department2 name:{0:16}Manger:{1:10}COUSE_FEES  {2:<12.2f}the end!'.format(department2,depart2_m,COUSE_FEES_Man)
length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)


line1 = f'department1 name:{department1:16}Manger:{depart1_m:10}COUSE_FEES  {COUSE_FEES_AV:<12.2f}the end!'
line2 = f'department2 name:{department2:16}Manger:{depart2_m:10}COUSE_FEES  {COUSE_FEES_Man:<12.2f}the end!'

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)

if __name__ == '__main__':
    pass