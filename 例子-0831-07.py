#coding=utf-8

#打开文件
file=open('/home/heygor/0831/txl.txt','r')
for i in file.readlines():
	#print(i)
	#print(type(i))
	i=i.strip('\n')
	#把字符串按照空格拆分
	b=i.split(' ')
	#print(b)
	#print(type(b))
	if b[-1]=='18028768679':
		print('tel in here！')
	else:
		print('not here')
file.close()
