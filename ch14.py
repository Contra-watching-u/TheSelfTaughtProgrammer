class Square:
    square_list = []
    def __init__(self,len):
        #square_list.append(self) remenber 'self.'
        self.square_list.append(self)
        self.len = len
    def __repr__(self):
        #print('{} by {} by {} by {}'.format(len,len,len,len)) __repr__ must return
        return '{} by {} by {} by {}'.format(self.len,self.len,self.len,self.len)
def conpare(obj1,obj2):
    print(obj1 is obj2)
sq1 = Square(12)
print(Square.square_list)
print(sq1)
sq2 = sq1
conpare(sq1,sq2)
