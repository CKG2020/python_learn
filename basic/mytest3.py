# 10月２３日
# yelid的使用
#send 送进去　　yield　扔出去

# def xxx():
#     print("xxx")
#     yield 2
#     yield 3
#
#
#
# x=xxx()
# print(type(x))  #<class 'generator'>
# y=next(x)
# print(y)
# y=x.send(6)
# print(type(y))  #<class 'int'>
# print(y)
# y=next(x)
# print(m)
# print(y)
# y=next(x)
# print(y)
# y=x.send(5)
# print(y)
# # x.send(null)
# print(y)


#类的学习

# class T (object):
#     print("xxxx")
# print(type(T))    #<class 'type'>　　此处会打印xxx python属于解释型语言　此处就相当于我在执行下面的ｔｙｐｅ语句
# t=T()         #class '__main__.T'>
# print(type(t))



# 在这里Ｊａｖａ复习了三种面向对象的方式　　定义式　组合式　　集合式
#定义式普通的最常用的Ｊａｖａ定义类和使用类的方法
#组合式　　　　定义一个类　里面定义了一个另一个类的对象作为一个属性
#集合式　　　一个类继承hashmap里面可以无限制的增加属性　作为ｋｅｙ　ｖ　对


# C++采用的是一个　ｓｔｒｕｃｔ　　Ａ　里面使用另一个ｓｔｒｕｃｔ　　Ｂ　属于上面的组合式这种情况　　并称之为继承　因为Ａ
# 里面占有Ｂ的内存
#　　当　Ａ里面是　　Ｂ　＊b的时候就不是继承了　是属于依赖式的注入

##而Ｐｙｔｈｏｎ使用的是集合式的　所以Ｐｙｔｈｏｎ类的属性约等于可以无限的增加　


# XX=type("TTT",(object,),{})  #这一句话是定义类的本质  第一个参数类名　第二个参数基类　　最后一个代表ｈａｓｈｍａｐ
#                             #所有的类都是一个hashmap
# x=XX()
# print(type(x))  #<class '__main__.TTT'>




###
# class P:
#     pass
#
# p=P();
# p.xxx=lambda x,y:x+y    #此处相当于在　Ｐ类里面加入了一个　key 为xxx的东西
# print(p.xxx(1,2))
#解释型语言就是解释一句执行一句　编译类型语言就是　将一个语言解释为另一个语言

#
# class TT:
#     x=1
#     def xxx(self):
#         pass
# print(vars(TT))  #这两句话效果一样
# print(TT.__dict__)
# t=TT
# t.yyy=1
# t.x=1
# print(vars(t))





#装饰器   天生的ＡＯＰ
def fun(f):
    print("-------------")
    f()
    print("==============")
@fun
def ff():
    print("xxx")


# fun(ff) 等同于上面的@fun



