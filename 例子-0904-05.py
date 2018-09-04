#coding=utf-8
class test(object):
        #类的属性
        a=100
        def __init__(self,b):
                #实例属性
                self.b=b
t=test(100) #实例化属性
#通过实例化对象访问类的属性
print('t.a=%d'%t.a)
#通过类名访问类的属性
print('test.a=%d'%test.a)
#通过实例化对象访问实例属性
print('t.b=%d'%t.b)
#通过类名访问实例属性
print('test.b=%d'% test.b)
