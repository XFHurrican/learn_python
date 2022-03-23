class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name):
        self.name=name

x=C('Jack')
print(x.__dict__)
print(C.__dict__)
print(x.__class__)  #输出了对象所属的类
print(C.__bases__)
print(C.__base__)
print(C.__mro__)
print(A.__subclasses__())