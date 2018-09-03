#coding=utf-8
def print_name(name):
	print('your name is %s' % name)

print_name('heygor')
#实参位置
def animal(pet1,pet2):
        print(pet1+'wang!!!'+pet2+'miao~~~')
#调用函数并且传入两个参数
#animal('cat','dog')
animal('dog','cat')
print('---------------')
def animal(pet1,pet2):
        print(pet1+'  wang!!!'+pet2+'  miao~~~')

animal(pet2='mimi',pet1='erha')

print('---------------')

def animal(pet2,pet1='erha'):
        print(pet1+'wang!!!'+pet2+'miao~~~')

#调用函数传入实参
animal('bosi')
animal('pig','out man')


print('---------------')
def test(x,y,*args):
        print(x,y,args)

test(1,2,'heygor','ladeng')

print('---------------')
def test1(x,y,**args):
        print(x,y,args)

test1(1,2,a=6,b=7,c='heygor')






