class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return (self.base * self.height) * 1/2

    def area2(self):
        return (self.base * self.height) * 1/2


triangle1 = RightTriangle(3, 4)
print("The area of triangle1 is", triangle1.area())

triangle2 = RightTriangle(2, 2)
print("The area of triangle2 is", triangle2.area2())

