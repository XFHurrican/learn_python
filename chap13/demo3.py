class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, stu_number):
        super().__init__(name, age)
        self.stu_number = stu_number

class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear

class MaleTeacher(Teacher):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age,teachofyear)

stu=Student('张三', 20, '1001')
teacher = Teacher('李四', 34, 10)
MaleTeacher = MaleTeacher('王五', 34, 10)
stu.info()
teacher.info()
MaleTeacher.info()
MaleTeacher.teachofyear