#!/usr/bin/python3.7
# -*- coding=utf-8 -*-


import os


# 已创建过如下文件夹，所以再次创建会报错

# os.mkdir('test')
#
# os.chdir('test')
#
# qytang1 = open('qytang1','w')
#
# qytang1.write('test file\n')
#
# qytang1.write('this is qytang\n')
#
# qytang1.close()
#
# qytang2 = open('qytang2','w')
#
# qytang2.write('test file\n')
#
# qytang2.write('qytang python\n')
#
# qytang2.close()
#
# qytang3 = open('qytang3','w')
#
# qytang3.write('test file\n')
#
# qytang3.write('this is python\n')
#
# qytang3.close()
#
# os.mkdir('qytang4')
#
# os.mkdir('qytang5')


print('文件中包含“qytang"关键字的文件为:')

# os.chdir('test')  #进入test文件夹


for root,dirs,files in os.walk(os.getcwd()+'/test',topdown=False):
    # print(files)
    for i in range(len(files)):
        if 'qytang' in files[i]:  # 可能不对，qytang in files，巧了这个files的名字也是qytang而已
            print(files[i])


for root,dirs,files in os.walk(os.getcwd()+'/test',topdown=False):
    for name in files:
        # print(os.path.join(root,name))
        os.remove(os.path.join(root,name))
    for name in dirs:
        # print(os.path.join(root,name))
        os.rmdir(os.path.join(root,name))


os.removedirs('test')



if __name__ == '__main__':
    pass