#coding=utf-8
def test():
	n=1
	print('first')
	yield n
	n+=1
	print('second')
	yield n
	n+=1
	print('third')
	yield n

a=test()
print('next one')
print(next(a))

print('next one')
print(next(a))


print('next one')
print(next(a))


print('next one')
print(next(a))
