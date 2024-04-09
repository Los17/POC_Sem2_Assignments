
class Rectangle:

    def __init__(self, base: float, height: float) -> None:
        if (base < 0):
            self.__base = 0
        else:
            self.__base = base
        if (height < 0):
            self.__height = 0
        else:
            self.__height = height
   
    def get_height(self) -> float:
        return self.__height
    
    def get_base(self) -> float:
        return self.__base

    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
   
    def get_area(self) -> float:
        return self.__base * self.__height

    def __str__(self) -> str:
        return "Rectangle with base:" + str(self.__base) + ",height:" + str(self.__height)

class Square (Rectangle):
    def __init__(self, side: float) -> None:
          super().__init__(side, side)
          self.__.side = side

    def get_side(self) -> float:
        return self.__side

    def __str__(self) -> str:

        return "Square with side length:" + str(self.__side)


square1 = Square (5)
print(square1)
print("The area of square1 is", square1.getarea())