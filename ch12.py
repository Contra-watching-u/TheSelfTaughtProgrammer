#1
class Apple:
    def __init__(self,size,weight,color,taste):
        self.size = size
        self.weight = weight
        self.color = color
        self.taste = taste

#2
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        import math
        return math.pi*self.radius**2
#3
class Triangle:
    def __init__(self,height,base):
        self.height = height
        self.base = base
    def area(self):
        return self.height*self.base/2

#4
class Hexagon:
    def __init__(self,radius):
        self.radius = radius
    def calculate_perimeter(self):
        return self.radius*6
#different from my image...but this is'nt wrong.
