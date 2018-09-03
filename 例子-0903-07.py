#coding=utf-8
sum=lambda a1,a2:a1+a2
print('相加后的值是:',sum(10,20))
print('------------------')
stu=[{'name':'tom','age':18},{'name':'jerry','age':20},{'name':'snoopy','age':30}]

stu.sort(key=lambda x:x['name'])
print(stu)

stu.sort(key=lambda x:x['age'])
print(stu)

print('----------------------------')
def operation(a,b,opt):
        re=opt(a,b)
        return re

num1=int(input('数字1：'))
num2=int(input('数字2：'))
result=operation(num1,num2,lambda a,b:a+b)
print(result)

