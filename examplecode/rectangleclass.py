class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def get_area(self):
        return self.length * self.width
    
    def compare_size(self, rect1):
        area1 = self.get_area()
        area2 = rect1.get_area()
        if area1 < area2:
            return True
        else:
            return False
    def tell_square(self):
        if self.length == self.width:
            return True
        else:
            return False
        
def compare_rect_size(rect1, rect2):
    area1 = rect1.get_area()
    area2 = rect2.get_area()
    if area1 < area2:
        return True
    else:
        return False
        

r1 = Rectangle(2,3)
r2 = Rectangle(3,4)
r3 = Rectangle(2,3)
r4 = Rectangle(5,5)

print(r1.get_area())
print(r1.tell_square())
print(r1.compare_size(r2))
print(r4.tell_square())
print(compare_rect_size(r1, r2))

