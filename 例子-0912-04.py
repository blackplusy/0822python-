#coding=utf-8
import multiprocessing as mp

def job(a,d):
	print(a+d)

if __name__=='__main__':
	p1=mp.Process(target=job,args=(2,4))
	p1.start()
	p1.join()
