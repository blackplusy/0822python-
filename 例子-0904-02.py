#coding=utf-8
#class student:
#	def __init__(self):
#		self.boy=20
#		self.girl=30
#	def study(self):
#		print('good good study!!!')
#
#simida=student()
#print(simida.boy)
#print(simida.girl)
#simida.study()

print('*********************')
class student:
	def __init__(self,boy,girl):
		self.badboy=boy
		self.cutegirl=girl
	def study(self):
		print('study')
z=student(20,30)
print('班级中男生有%d 个'%z.badboy)
print('班级中女生有%d 个'%z.cutegirl)
