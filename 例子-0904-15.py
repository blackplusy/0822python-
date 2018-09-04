#coding=utf-8
import time
def dec(func):
	def jisuan(a,b):
		starttime=time.time()
		func(a,b)
		endtime=time.time()
		sec=endtime-starttime
		print('time is %d'%sec)
	return jisuan




@dec
def func(a,b):
	print('a+b=?')
	time.sleep(1)
	print('its',a+b)

f=func
f(4,5)
