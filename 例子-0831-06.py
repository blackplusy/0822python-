#coding=utf-8
import csv

with open('/home/heygor/0831/txl.csv','r') as f:
	reader=csv.reader(f)
	for i in reader:
		print(i)


with open('/home/heygor/0831/txl2.csv','w') as f:
	file=csv.writer(f,dialect='excel')
	file.writerow([1,2,3,4])
	file.writerow([11,22,33,44])
