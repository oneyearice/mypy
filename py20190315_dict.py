qytang_dict = {'公司':
                   {'乾颐堂':
                        {'部门':
                             [{'部门名':'Python',
                              '师资':['秦柯','教主'],
                              '课程':["Python基础",
                                    "Python网络编程 第一部分 经典协议",
                                    "Python网络编程 第一部分 经典协议",
                                    "Python网络编程 第一部分 经典协议"
                                    ]

                              }
                             ]
                         }

                   }


               }

if __name__ == "__main__":
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(qytang_dict)
