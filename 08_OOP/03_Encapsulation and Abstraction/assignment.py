class Rectangle:
    def __init__(self, base: float, height: float) -> None:
        if(base < 0):
            self.__base = 0
        else:       
            self.__base = base
            
        if(height < 0):
            self.__height = 0
        else:
            self.__height = height
        
    def get_height(self) -> float:
        return self.__height
    
    #YOUDO the get_base method
    def get_base(self) -> float:
        return self.__base
    
    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
    
    #Youdo get_area method
    def get_area(self) -> float:
        return (self.__base * self.__height) /2
 
rectangle1 = Rectangle(3,5)
print("Height =", rectangle1.get_height())
print("Base =", rectangle1.get_base())
print("Perimeter =", rectangle1.get_perimeter())
print("Area =", rectangle1.get_area())

rectangle2 = Rectangle(10,5)
print("Height =", rectangle2.get_height())
print("Base =", rectangle2.get_base())
print("Perimeter =", rectangle2.get_perimeter())
print("Area =", rectangle2.get_area())

#YOUDO>  create two rectangles.  print their base, height, perimeter, and area
#using only the methods not the fields/property/attributes
