import math
class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        if  not ((isinstance(x, int) or isinstance(x, float)) or (isinstance(y, int) or isinstance(y, float))):
            raise TypeError("Podaleś niepoprawny typ punktu")
        self.x = float(x)
        self.y = float(y) 


    def __str__(self):      # zwraca string "(x, y)"
        return "({}, {})".format(self.x,self.y)

    def __repr__(self):        # zwraca string "Point(x, y)"
        return "Point({}, {})".format(self.x,self.y)

    def __eq__(self, other):  # obsługa point1 == point2
        return self.x==other.x and self.y==other.y

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other): # v1 - v2
        return Point(self.x-other.x, self.y-other.y)

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny
        return Point(self.x*other.x, self.y*other.y)

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return math.sqrt(self.x**2+self.y**2)
    
    def __hash__(self):
        return id((self.x, self.y))

    def as_tuple(self):
        return (self.x, self.y)