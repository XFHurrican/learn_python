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
stu2=Student('李四',20)
stu1.eat()                  #对象名.方法名
stu1.method()
stu1.classmethod()
print(stu1.name,stu1.age)

print('---------------------')
print(Student.eat(stu1))    #类名.方法名（对象）
print(stu1.native_place)
print(stu2.native_place)
Student.native_place='天津'
print(stu1.native_place)
print('-----------类方法的使用方式-----------')
Student.classmethod()
print('-----------静态方法的使用方式-----------')
Student.method()
print('-----------静态方法的使用方式-----------')