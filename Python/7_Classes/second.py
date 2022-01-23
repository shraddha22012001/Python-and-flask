import math

class Shape:

    def __init__(self, color='black', filled=False):
        self.__color = color
        self.__filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled
    def display_parent(self):
        print(" Parent Class")


class Quadrilateral(Shape):

    def __init__(self, length, breadth):
        Shape.__init__(self)
        self.__length = length
        self.__breadth = breadth

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_breadth(self):
        return self.__breadth

    def set_breadth(self, breadth):
        self.__breadth = breadth
    def display_parameters_quad(self):
        print("Length :",self.__length)
        print("Breadth :",self.__breadth)
        
    def get_area(self):
        return self.__length * self.__breadth



class Triangle(Shape):
    def __init__(self, base, height):
        Shape.__init__(self)
        self.__base = base
        self.__height = height

    def get_base(self):
        return self.__base

    def set_base(self, base):
        self.__base = base
    
    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height
    def display_parameters_tri(self):
        print("Height :",self.__height)
        print("Base :",self.__base)

    def get_area(self):
        return 0.5 * self.__base * self.__height

class child(Quadrilateral,Triangle):
     def __init__(self,x,y):
        Quadrilateral.__init__(self, x,y)
        Triangle.__init__(self, x,y)
        

     def display_child(self):
        print("Child Class")
s = Shape()
print("Parent class 'Shape' :")
s.display_parent()

q1 = Quadrilateral(10, 5)
print("\n\nQuadrilateral i.e Child of Shape class:")
print("Area of Quadrilateral:", q1.get_area())
print("Color of Quadrilateral:", q1.get_color())
print("Is Quadrilateral filled ? ", q1.get_filled())
q1.set_filled(True)
print("Is Quadrilateral q1 filled ? ", q1.get_filled())
q1.set_color("orange")
print("Color of Quadrilateral:", q1.get_color())
q1.display_parameters_quad()

c1 = Triangle(12,6)
print("\n\nTriangle i.e Child of Shape class:")
print("\nArea of Triangle:", format(c1.get_area(), "0.2f"))
print("Color of Triangle:", c1.get_color())
print("Is Triangle filled ? ", c1.get_filled())
c1.set_filled(True)
print("Is Triangle filled ? ", c1.get_filled())
c1.set_color("blue")
print("Color of Triangle:", c1.get_color())
c1.display_parameters_tri()

b = child(10,10)
print("\n\nChild of quadrilateral and triangle class:")
print("Is Shape filled ? ", b.get_filled())
b.set_color("pink")
print("Color of shape:", b.get_color())
b.display_parameters_tri()
b.display_parameters_quad()
b.set_height(20)
b.set_base(10)
b.display_parameters_tri()
b.display_child()
