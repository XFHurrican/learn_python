a=20
b=100
c=a+b
d=a.__add__(b)
print(c,d)

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name

stu1=Student('张三')
stu2=Student('李四')

s=stu1+stu2
print(s)

s=stu1.__add__(stu2)
print(s)

lst=[11,22,33,44]
print(len(lst))
print(lst.__len__())
