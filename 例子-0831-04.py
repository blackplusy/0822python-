#coding=utf-8
dic={'name':'heygor','QQ':914338492}
#dic2={'name':'mayun','QQ':100000000}

print(dic)
#print(dic2)

dic['name']='8jie'
print(dic)
dic['QQ']=110
print(dic)

print('________________________')
dic={'name':'heygor','tel':110}
print(dic)
del dic['name']
print(dic)
#del dic
#print(dic)

print('________________________')
dic={'name':'simida','tel':119}
print(dic)
dic.clear()
print(dic)


print('________________________')
dic={'name':'heygor','tel':18000000000}
print(dic.keys())

for i in dic.keys():
	print(i)


print('________________________')
dic={'name':'heygor','tel':18000000000}
print(dic.values())

for i in dic.values():
	print(i)

print('________________________')
dic={'name':'heygor','tel':18000000000}
for i,j in dic.items():
	print(i,j)











