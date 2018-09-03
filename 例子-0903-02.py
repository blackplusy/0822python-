#coding=utf-8
#1.无参数，无返回值
def print_hello():
	print('hello world')

print_hello()


#2.无参数有返回值
def sleep():
	return 'sleep!!!!!'

s=sleep()
print(s)

#3.有参数，无返回值
def sub(x,y):
	print('x+y=',x+y)
sub(2,3)

#4.有参数，有返回值
def sub(x,y):
	return x+y
res=sub(20,10)
print(res)

