from points import Point
import math

class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        """Konstruktor"""
        if self.check_collinear(x1, y1, x2, y2, x3, y3):
           raise ValueError("Punkty leżą na jednej prostej")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):        # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "[({}, {}), ({}, {}), ({}, {})]".format(self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y,self.pt3.x,self.pt3.y)

    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return "Triangle({}, {}, {}, {}, {}, {})".format(self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y,self.pt3.x,self.pt3.y)


    def __eq__(self, other):   
        """sprawdza tr1 == tr2"""
        set1=set([self.pt1, self.pt2, self.pt3])
        set2=set([other.pt1, other.pt2, other.pt3])
        return set1==set2

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):          # zwraca środek trójkąta
        return Point((self.pt1.x+self.pt2.x+self.pt3.x)/3,(self.pt1.y+self.pt2.y+self.pt3.y)/3)

    def area(self):           # pole powierzchni
        a1=self.pt1.x*(self.pt2.y-self.pt3.y)
        a2=self.pt2.x*(self.pt1.y-self.pt3.y)
        a3=self.pt3.x*(self.pt1.y-self.pt2.y)
        A=a1-a2+a3
        return math.fabs(A/2)

    def move(self, x, y):     # przesunięcie o (x, y)
        pt=Point(x,y)
        pt1=self.pt1 + pt
        pt2=self.pt2 + pt
        pt3=self.pt3 + pt
        return Triangle(pt1.x, pt1.y, pt2.x, pt2.y, pt3.x, pt3.y)

    def check_collinear(self, x1, y1, x2, y2, x3, y3):
        """sprawdza czy punkty są kolinearne"""
        area = a = x1 * (y2 - y3) +   x2 * (y3 - y1) +  x3 * (y1 - y2)
        return area==0
    
    def make4(self):
        """zwraca krotkę czterech mniejszych trójkątów"""
        pt1_half_pt2=Point((self.pt1.x + self.pt2.x) / 2,(self.pt1.y + self.pt2.y) / 2)
        pt2_half_pt3=Point((self.pt2.x + self.pt3.x) / 2,(self.pt2.y + self.pt3.y) / 2)
        pt1_half_pt3=Point((self.pt1.x + self.pt3.x) / 2,(self.pt1.y + self.pt3.y) / 2)

        tr1 = Triangle(*self.pt1.as_tuple(),*pt1_half_pt2.as_tuple(), *pt1_half_pt3.as_tuple() )
        tr2 = Triangle(*pt1_half_pt2.as_tuple(), *pt1_half_pt3.as_tuple(), *pt2_half_pt3.as_tuple() )
        tr3 = Triangle(*pt1_half_pt2.as_tuple(), *self.pt2.as_tuple(), *pt2_half_pt3.as_tuple())
        tr4 = Triangle(*pt2_half_pt3.as_tuple(), *self.pt3.as_tuple(), *pt1_half_pt3.as_tuple())

        return (tr1, tr2, tr3, tr4)
    def __hash__(self):
        return id([self.pt1, self.pt2, self.pt3])


