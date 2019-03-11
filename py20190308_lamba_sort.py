# port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
# port_list_tran = [eth('1','101','1','42'),eth('1','101','1','26'),eth('1','101','1','7'),]
# sorted(port_list_tran,key=lambda eth:eth.)
#
#


# for x in port_list:
#     result = (x.split('/'))
#     first = result[2]
#
#
#
#
#     print(result[3])
#     print ('/'.join(result))
#     # print(x)
# # result_port_list = port_list[1]
# # print(result_port_list)
# #
# # # sorted(port_list,key=lambda )
#
# # port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
# x = 'eth 1/101/1/42'
# print(x[4])
# # port_list_tran = ['eth',1,101,1,42)]
# class Student:
#     def __init__(self, name, grade, age, mo):
#         self.name = name
#         self.grade = grade
#         self.age = age
#         self.mo= mo
#
#     def __repr__(self):
#         return repr((self.name, self.grade, self.age, self.mo))
# student_objects = [
#     Student(1,101,1,42),
#     Student(1,101,1,26),
#     Student(1,101,1,7),
# ]
#
#
# print(sorted(student_objects, key=lambda student: student.mo))
#
#

port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
# y = 'eth 1/101 /  1   /   4  2'
     # 012345678 9  10  11  12 13
port_list_first = sorted(port_list,key=lambda x:(int(x[10]),int(x[12:])))
print(port_list_first)
