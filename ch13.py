class Shape():
    def what_am_i(self):
        print('I am a shape')
class Rectangle(Shape):
    def __init__(self,l1,l2,l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
    def calculate_perimeter(self):
        return self.l1+self.l2+self.l3

class Square(Shape):
    def __init__(self,l1,l2):
        self.l1 = l1
        self.l2 = l2
    def calculate_perimeter(self):
        return (self.l1+self.l2)*2
    def change_size(self,d1,d2):
        self.l1 += d1
        self.l2 += d2
        if (self.l1 <= 0) or (self.l2 <= 0):
            print('shape can\'t exist!')
rec1 = Rectangle(11,22,33)
sq1 = Square(11,22)
rec1.what_am_i()
print(rec1.calculate_perimeter())
print(sq1.calculate_perimeter())
sq1.change_size(10,20)
print(sq1.calculate_perimeter())
class Horse:
    def __init__(self,name,rider):
        self.name = name
        self.rider = rider
class Rider:
    def __init__(self,name):
        self.name = name
rider1 = Rider('Take')
horse = Horse('DeepInpact',rider1)
print(horse.rider.name)
