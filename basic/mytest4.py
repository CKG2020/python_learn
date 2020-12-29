# class  T:
#     def  __init__(self,a,b):
#         self.a=a
#         self.b=b
# t=T("xxx","yyy")
# # print(t.a)
# # print(t.b)
# print(vars(t))
# # # {'b': 'yyy', 'a': 'xxx'}
# # # 类似做出私有属性的感觉　　＿＿ａ不能直接点出来
# class  T:
#     def  __init__(self,a,b):
#         self.__a=a
#         self.b=b
# t=T("xxx","yyy")
# print(vars(t))
# # {'b': 'yyy', '_T__a': 'xxx'}
# print(t._T__a)

class A:
    def xxx(self):
        print("xxx")
class B:
    def xxx(self):
        print("yyy")
class C:
    pass
class T(A,B):
            pass
print(T.__mro__)# (<class '__main__.T'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
                # #Ｔ从右向左继承　先继承B　　再继承A
t=T()
t.xxx()  #xxx
class T(B,A):
    pass
print(T.__mro__)# (<class '__main__.T'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
t=T()
t.xxx()  #yyy
print(T.__base__)  #<class '__main__.B'>  最后一个继承的类　　　
print(T.__bases__) #(<class '__main__.B'>, <class '__main__.A'>)
T.__bases__=(C,B)   #也算是另一种是实现继承的方式
print(T.__base__)
t=T
print(t.__mro__)
print(T.__mro__)  #(<class '__main__.T'>, <class '__main__.C'>, <class 'object'>)