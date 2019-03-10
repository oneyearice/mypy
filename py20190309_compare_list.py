list1 = ['aaa',111,(4,5),2.01]
list2 = ['bbb',333,111,3.14,(4,5)]

# for the basic logic

# for x in list1:  # 取出list1的第一个字符
#
#     for y in list2:  #  拿list2中的所有字符进行比较
#         if x == y:
#             result = 1  # 如果出现相同字符，则计为1
#             break  # 随机x不再继续和list2里后面的字符进行比较
#             # print(result)
#             # print(x, 'in List1 and List2')
#         else:  # 如果x和list2中的当前字符不同，则计为0，然后继续和list2中下一个字符比较继续进行本轮for循环
#             result = 0
#             # print(result)
#     # print(result)
#     if result:  # 如果结果为1，则打印，注意打印要在x一轮比较完结后再打印，也就是在第一轮for子层级进行打印
#         print(x,'both in list1&2')
#     else:  # 如果结果为0，则打印
#         print(x,'only in list1')


#  the basic logic transform to def
#
# def compare(a,b):
#     for x in list1:  # 取出list1的第一个字符
#         for y in list2:  #  拿list2中的所有字符进行比较
#             if x == y:
#                 result = 1  # 如果出现相同字符，则计为1
#                 break  # 随机x不再继续和list2里后面的字符进行比较
#                 # print(result)
#                 # print(x, 'in List1 and List2')
#             else:  # 如果x和list2中的当前字符不同，则计为0，然后继续和list2中下一个字符比较继续进行本轮for循环
#                 result = 0
#                 # print(result)
#         # print(result)
#         if result:  # 如果结果为1，则打印，注意打印要在x一轮比较完结后再打印，也就是在第一轮for子层级进行打印
#             print(x,'both in list1&2')
#         else:  # 如果结果为0，则打印
#             print(x,'only in list1')
#
# print(compare(list1,list2))



# The best way

# for x in list1:  # 取出list1的第一个字符
#
#     if x in list2:
#         print(x,'both in list1 and list2')
#     else:
#         print(x,'only in list1')

# the best way transform to def

def compare(a,b):
    for x in list1:  # 取出list1的第一个字符
        if x in list2:
            print(x,'both in list1 and list2')
        else:
            print(x, 'only in list1')

compare(list1,list2)
