#coding=utf-8
class student:
	def __init__(self,name):
		self.name=name
	def info(self):
		print('你的名字是%s'% self.name)

def studentinfo(student):
	student.info()
#heygor是student类的实例化对象
heygor=student('heygorgaga')
#对象实例化之后可以使用类的方法
studentinfo(heygor)
#studentinfo括号中传入的heygor是一个已经实例化的对象调用类的方法

o8ma=student('o8ma')
studentinfo(o8ma)


