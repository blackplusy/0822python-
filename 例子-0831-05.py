#coding=utf-8
file=open('/home/heygor/0831/test','r')
for i in file:
        print(i)
file.close()

print('------------------')
str1='heygor so cool!!!'
file=open('/home/heygor/0831/memeda','w')
file.write(str1)
file.close()

print('------------------')

file=open('/home/heygor/0831/memeda','a')
file.write('\n5kong 120')
file.close()


print('------------------')

