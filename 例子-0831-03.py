#coding=utf-8
a=(1)
print(a)
#补充：type() 类型
print(type(a))
a=(1,)
print(a)
print(type(a))


#访问元组
tup=(1,2,3,4,5)
for i in tup:
        print(i)


#删除元组
tup=(1,2,3)
del tup
#print(tup)

print('______________________')
tup=(1,2,3,4,5)
print(tup[0])
print(tup[-2])
print(tup[2:4]) #4
print(tup[3:])  #45
print(tup[:3])  #123


print('______________________')
tup=(1,2,3,4,3,2,8)
print(len(tup))
print(max(tup))
print(tup.index(8))
print(tup.count(2))







