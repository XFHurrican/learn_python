class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('启动汽车引擎')
car=Car('宝马')
car.start()
print(car.brand)