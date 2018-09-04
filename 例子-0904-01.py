#coding=utf-8
class student:                             #定义类
        def study(self):                   #方法列表
                print('im study!!!!')
        def play(self):                    #方法列表
                print('play ball')

boy=student()
#产生一个student的对象，通过boy实例对象来访问属性和方法
boy.age=20
#给对象添加属性，注意：后面如果再次出现，表示对属性进行修改
boy.favor='sport'
#给对象添加属性
boy.study()
#通过实例对象访问类的方法
boy.play()
print(boy.age)
print(boy.favor)
