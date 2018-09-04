#coding=utf-8
class a:
        def printa(self):
                print('------------a------------')

class b:
        def printb(self):
                print('-----------b------------')

class c(a,b):
        def printc(self):
                print('-----------c------------')
c1=c()
c1.printa()
c1.printb()
c1.printc()
