# class decro1:
#     def __init__(self,clz):
#         self.clz=clz #Eng1
#
#     def __call__(self, *args, **kwargs):
#         class prof:
#             def __init__(self,couse):
#                 self.couse=couse     #couse存储了Eng1的对象
#
#             def getContent1(self):
#                 return self.couse.getContent1()+"|ZH|MATH"
#         return prof(self.clz())
#
# @decro1
# class Eng1:
#     def __init__(self):
#         print("00000000")
#     def getContent1(self):
#         return "ENG"
#
# class Eng2:
#     def getContent1(self):
#         return "ENG2"
#
# c=Eng1()
# print(c.getContent1())
# print("--------------------------")
#
# d=decro1(Eng2)
# c=d.__call__()
# print(c.getContent1())
#
# print("="*50+"13")

# class Person:
#
#     def __init__(self,id,name):
#         print("Person init")
#         self.__id=id
#         self.__name=name
#
#     @staticmethod
#     def run():
#         print("runing...")
#
#     @classmethod      #比staticmethod默认多传入一个类类型
#     def newInstance(clz,id,name):
#         print("classmethod: "+str(clz))
#         return clz(id,name)
#
#     def __str__(self):
#         return "str id: "+str(self.__id)+" name: "+self.__name
#
# if __name__ == "__main__":
#     Person.run()
#     p=Person.newInstance(2,"ccc")
#
#     # p=eval("Person").newInstance(2,"ccc")
#
#     print("="*50)
#
#     a=1
#     print("1: "+str(type(a)))
#     print("1: "+str(a.__class__))
#     print("1: " + str(type(a.__class__)))
#     print(type(Person))
#     print(type(p))
#     print(p.__class__)
#
#     print(p)

# class Some:
#     print("fjsdhfhsdhfksdfhj")
#     __pppp=""
#     def __init__(self,xx,pp):
#         self.xx=xx
#         self.__pp=pp
#
#     def xxx(self):
#         print("---xxx---")
#         pass
#
# print(dir(Some))
# print()
# s=Some("aaa","bbb")
# s.ppppppp=1000
# print(s.__dict__)
# print(dir(s))
# #
# print(getattr(s,'xx'))
# # getattr(s,'__pp')
# print( callable(getattr(s,'xxx')))
# print( callable(getattr(s,'__doc__')))
# methodLIst = [method for method in dir(s) if callable(getattr(s,method))]
# print(methodLIst)
#
# print("="*50+"1")
# #=====================自省机制=======================================
#
# pprint(globals())
# print()
# import sys
#
# pprint(globals())
# print()
# s = globals()["Some"]
# s("aaa","bbb").xxx()

class Some:
    def __init__(self):
        print("__init__")
    # def __new__(cls, *args, **kwargs):
    #     print("__new__")

    # def __call__(self, *args, **kwargs):
    #     print("__call__")

# s=Some()
# print(type(s)())  #int a=1 ;delctype a b;b=2
# Some()
# Some.__call__() #__call__就是括号运算符
#

def xxx(arg):
    print(arg)

xxx(100)
xxx.__call__(100)

print("="*50+"1")