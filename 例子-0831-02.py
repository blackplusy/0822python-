#coding=utf-8
#给定列表进行操作
a=[1,2,3,4,5,6,7,8,9,10]
print([3*x for x in a])
print('*********************')

#没有给定列表可以用range()方法
print([3*x for x in range(1,11)])

#加入if条件进行列表推到
#获取列表a中所有的偶数

print([x for x in a if x % 2 ==0])

print('_______________________')
#多个for语句进行列表推到
print([[x,y] for x in range(2) for y in range(2)])

