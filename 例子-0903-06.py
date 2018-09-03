#coding=utf-8
#嵌套函数
def test1():
	print('im in test1！！')

def test2():
	test1()
	print('im in test2!!!')

def test3():
	test2()
	print('im in test3')

test3()

def func(n):
        print('进入第%d层梦'%n)
        if n==3:
                print('进入潜意识区')
        else:
                func(n+1)
        print('从第%d层梦中醒来'%n)

func(1)

