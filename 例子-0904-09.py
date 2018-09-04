#coding=utf-8
class people:
	country='china'
	@classmethod
	def getcountry(cls):
		return cls.country
	@classmethod
	def setcountry(cls,country):
		cls.country=country


p=people()
print(p.getcountry())
p.setcountry('USA')
print(p.getcountry())
