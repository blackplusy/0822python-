#coding=utf-8
class dog:
        def __init__(self,name,color='black'):
                self.name=name
                self.color=color
        def run(self):
                print('狗富贵，互相汪！！')

class taidi(dog):
        def set_name(self,name):
                self.name=name
        def eat(self):
                print('im eating!!')

gou=taidi('泰迪')
print('名字为%s'%gou.name)
print('颜色是%s'%gou.color)
gou.eat()
gou.set_name('erha')
print('旺财的新名字',gou.name)
gou.run()

