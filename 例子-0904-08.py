#coding=utf-8
class people:
        country='china'
        @classmethod
        def getcountry(cls):
                return cls.country
p=people()
print(p.getcountry()) #实例对象调用类的方法
print(people.getcountry())
