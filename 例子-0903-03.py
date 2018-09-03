#coding=utf-8
def sum(a,b):
	jisuan=a+b
	return jisuan

s=sum(20,30)
print(s)

print('----------------------')
def re(a,b):
	a*=10
	b*=10
	return a,b

num=re(3,5)
print(num)
print(type(num))
print('----------------------')
r1,r2=re(3,4)
print(r1,r2)
print(type(r1))
print(type(r2))
