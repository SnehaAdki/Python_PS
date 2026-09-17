import math


class Line:

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        v1 = (x2-x1)**2
        v2 = (y2-y1)**2
        distance = math.sqrt(v1+v2)
        return distance

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        v1 = y2-y1
        v2 = x2-x1
        slope = v1/v2

        return slope

coo1 = (3,2)
coo2 = (8,10)
l1 = Line(coo1 , coo2)

print(l1.distance())
print(l1.slope())