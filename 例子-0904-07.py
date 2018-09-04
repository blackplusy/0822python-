#coding=utf-8
class student:
        def __init__(self,num):
                self.__num=num
        def print_name(self):
                print('your age is %d'%self.__num)
age=student(30)
age.print_name()

