#coding=utf-8
import threading
def job1():
	global A,lock
	lock.acquire()
	for i in range(10):
		A+=1
		print('job',A)
	lock.release()

def job2():
	global A,lock
	lock.acquire()
	for i in range(10):
		A+=10
		print('job2',A)
	lock.release()

lock=threading.Lock()
A=0
t1=threading.Thread(target=job1)
t2=threading.Thread(target=job2)
t1.start()
t2.start()
t2.join()
t1.join()
