#coding=utf-8
def test1():
	a=10
	print('a的值是：',a)
	a=20
	print('a的新值',a)

def test():
	a=40
	print('test中的a是',a)
test1()
test()

print('********************************')
a=100
print('a的值是:',a)

def test01():
        a=20
        print('test01中a值是',a)

def test02():
        print('test2中a的值是',a)

test01()
test02()

print('********************************')
a=100
print('a的值是',a)

def test1():
        global a
        a=200
        print('test1中修改全局变量a',a)

def test2():
        print('test2中使用全局变量',a)

test1()
test2()
print('全局变量a的值是',a)

