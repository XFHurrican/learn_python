#第107课
class rectangle:
    def __init__(self,w,h):
        self.w,self.h=w,h
    def area(self):
        return self.w*self.h
    def perimeter(self):
        return 2*(self.w+self.h)

rect=rectangle(2,4)
print(rect.area(),rect.perimeter())