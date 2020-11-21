from points import Point
import math

class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):        # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "[({}, {}), ({}, {}), ({}, {})]".format(self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y,self.pt3.x,self.pt3.y)

    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return "Triangle({}, {}, {}, {}, {}, {})".format(self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y,self.pt3.x,self.pt3.y)


    def __eq__(self, other):    # obsługa tr1 == tr2
        return self.pt1==other.pt1 and self.pt2==other.pt2 and self.pt3==other.pt3

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):          # zwraca środek trójkąta
        return Point((self.pt1.x+self.pt2.x+self.pt3.x)/3,(self.pt1.y+self.pt2.y+self.pt3.y)/3)

    def area(self):           # pole powierzchni
        a1=self.pt1.x*(self.pt2.y-self.pt3.y)
        a2=self.pt2.x*(self.pt1.y-self.pt3.y)
        a3=self.pt3.x*(self.pt1.y-self.pt2.y)
        A=a1-a2+a3
       # P=(self.pt1.x*self.pt2.y+self.pt2.x*self.pt3.y+self.pt3.x*self.pt1.y-self.pt1.x*self.pt3.y-self.pt2.x*self.pt1.y-self.pt3.x*self.pt2.y)/2
        return math.fabs(A/2)

    def move(self, x, y):     # przesunięcie o (x, y)
        pt=Point(x,y)
        pt1=self.pt1+pt
        pt2=self.pt2+pt
        pt3=self.pt3+pt
        return Triangle(pt1.x,pt1.y,pt2.x,pt2.y,pt3.x,pt3.y)

