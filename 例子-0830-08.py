#coding=utf-8
#直接访问
li=['heygor','ladeng','o8ma']
print(li)

#遍历访问
for i in li:
	print(i)

#成员访问
print('heygor' in li)

print('*****************8888')
li=[1,2,3]
print(li[0])
print(li[-2])
#print(li[5])

print(li[:-1])  
print(li[1:])
print(li[1:2])

print('*****************8888')
li=[1,2,3]
li2=[4,5,6]
print(li+li2)


print('*****************8888')
li=[1,2,3]
print(li)
li[2]=100
print(li)
li[-1]=30
print(li)


print('*****************8888')
li=['a','b','c']
print(li)
del li[1]
print(li)

