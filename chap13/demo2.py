class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age      #年龄不希望在类的外部被使用
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
print(stu.show())
print(stu.name)
print(stu._Student__age)