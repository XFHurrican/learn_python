class Student:
    native_place='吉林'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #实例方法
    def eat(self):
        print('学生在吃饭')

    #静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod,所以我是静态方法')

    #类方法
    @classmethod
    def classmethod(cls):
        print('我使用了classmethod,所以我是类方法')

#在类之外定义的是函数，在类之内定义的是方法
def drink():
    print('喝水')

stu1=Student('许方浩',22)
print(id(stu1))
print(type(stu1))
print(stu1)
print('-----------------------')
print(id(Student))
print(type(Student))
print(Student)