#coding=utf-8
'''
li=[1,2,3,5,4]
print(li)
li.append('gaga')
print(li)
print(li.pop())
'''
#获取列表的索引
l=['heygor','ladeng','8ma']
print(l.index('ladeng'))

#python的enumerate函数，获取列表中中每个元素的索引和值

l1=['simida','kouniqiwa','haleshao']
for index,value in enumerate(l1):
	print('索引是：'+str(index)+' 值是：'+value)
