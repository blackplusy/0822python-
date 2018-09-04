#coding=utf-8
class animal:
        def jiao(self):
                print('ao~~~')
class dog(animal):
        def jiao(self):
                print('wang!!!')

class cat(animal):
        def jiao(self):
                print('miao')

def test(obj):
        obj.jiao()

a=animal()
a.jiao()

d=dog()
c=cat()
test(d)
test(c)
