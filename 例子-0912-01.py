#coding=utf-8
import threading
print(threading.active_count()) #获取当前线程数量
print(threading.current_thread())#查看当前运行的线程
#添加线程
def thread_job():
	print('当前线程是%s'%threading.current_thread())

def thread_job2():
	print('当前线程是%s'%threading.current_thread())
 
thread=threading.Thread(target=thread_job)
thread1=threading.Thread(target=thread_job2)
thread.start()
thread1.start()

