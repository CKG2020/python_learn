

if __name__ . __eq__ ("__main_"):
    print("xxx")
    print("----------")
if __name__ == '__main__':
    print("yyy")

# -*- coding: utf8 -*-
import copy
import sys
# 因为Python中有三种拷贝方式：浅拷贝、深拷贝和赋值拷贝。
#
# 赋值拷贝就像是定义新指针并指向了同一内存区域，对任意一个列表名进行操作，其他的也会变化。
#
# 深拷贝的作用是完全拷贝一个列表A并赋值给另一列表B
a = [1, 2, [3, 4]]
# b = copy.copy(a)    #浅拷贝
# c = copy.deepcopy(a) #深拷贝
# d = a
#
# print('address of a:', id(a))
# print('address of b:', id(b))
# print('address of c:', id(c))
# print('address of d:', id(d))
#
# print("=====================================")
# print('address of 1:', id(1))
# print('address of element 0 in a:', id(a[0]))
# print('address of element 0 in b:', id(b[0]))
# print('address of element 0 in c:', id(c[0]))
#
# print('a=', a)
# print('b=', b)
# print('c=', c)
# print('d=', d)
#
# print("=========================")
#
# a[0] = 99
# print('a=', a)
#
# print('b=', b)
#
# print('c=', c)
#
# print('d=', d)
#
# print
# 'address of element 0 in a:', id(a[0])
# print
# 'address of element 0 in b:', id(b[0])
# print
# 'address of element 0 in c:', id(c[0])
#
# print
# 'address of element 2 in a:', id(a[2])
# print
# 'address of element 2 in b:', id(b[2])
# print
# 'address of element 2 in c:', id(c[2])
#
# a[2].append(5)
# print
# 'a=', a
# print
# 'b=', b
# print
# 'c=', c
# print
# 'd=', d
#
#



# def test(param=[]):
#     print('address of param:', id(param))
#     param.append(1)
#     print('reference count of 1:', sys.getrefcount(1))
#     print(param)
#     return param
#
# print
# test(a)
# print
# test()
# print
# test()
# print
# 'a=', a
# print
# 'b=', b
# print
# 'c=', c
# print
# 'd=', d
#
# print
# 'reference count of 1:', sys.getrefcount(1)
# n = 1
# print
# 'reference count of 1:', sys.getrefcount(1)
# del n
# print
# 'reference count of 1:', sys.getrefcount(1)
