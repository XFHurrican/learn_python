class Animal:
    def eat(self):
        print('动物要吃东西')

class Dog(Animal):
    def eat(self):
        print('狗吃肉')

class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Person:
    def eat(self):
        print('人吃五谷杂粮')

def fun(cube):
    cube.eat()

fun(Animal())
fun(Dog())
fun(Cat())
fun(Person())