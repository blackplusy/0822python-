#coding=utf-8
import threading
import time
def t1():
	print('t1开始了')
	for i in range(10):
		time.sleep(0.1)
	print('t1结束')

def t2():
	print('t2开始')
	print('t2结束')

th1=threading.Thread(target=t1)
th2=threading.Thread(target=t2)
th1.start()
th2.start()
th2.join()
th1.join()
print('finished')
