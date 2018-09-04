#coding=utf-8
import time

def jisuan(func):
	def zsq():
		startime=time.time()
		func()
		endtime=time.time()
		sec=endtime-startime
		print('消耗时间为%d'%sec)

	return zsq

@jisuan
def func():
        print('hello')
        time.sleep(1)
        print('world')

f=func
f()
