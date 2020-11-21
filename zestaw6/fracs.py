import math
class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y
        self.simplify()
        self.check_zeroDiv()

    def __str__(self):        # zwraca "x/y" lub "x" dla y=1
        if self.y==1:
            return "{}".format(self.x)

        else:
            return "{}/{}".format(self.x,self.y)
           

    def __repr__(self):        # zwraca "Frac(x, y)"
        return "Frac({}, {})".format(self.x,self.y)

    # Python 2
    #def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Python 2.7 i Python 3
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        result=float(self-other)
        if result<0:
            return True
        else:
            return False
        

    def __le__(self, other):
        result=float(self-other)
        return result<=0

    #def __gt__(self, other): pass

    #def __ge__(self, other): pass

    def __add__(self, other): # frac1 + frac2
        x=self.x*other.y+other.x*self.y
        y=self.y*other.y
        
        return Frac(x,y)

    def __sub__(self, other):  # frac1 - frac2
        x=self.x*other.y-other.x*self.y
        y=self.y*other.y
        return Frac(x,y)

    def __mul__(self, other):   # frac1 * frac2
        x=self.x*other.x
        y=self.y*other.y
        return Frac(x,y)


    def __truediv__(self, other):  # frac1 / frac2
        if other.is_zero():
            raise ZeroDivisionError
        x=self.x*other.y
        y=self.y*other.x
        return Frac(x,y)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):       # float(frac)
        return float(self.x/self.y)

    def simplify(self):
        if self.y<0:
            self.x*=-1
            self.y*=-1
        a=math.gcd(self.x,self.y)
        self.x,self.y= self.x//a,self.y//a

    def is_zero(self):                # bool, typu [0, x]
        return self.x==0 and self.y!=0

    def check_zeroDiv(self):
        if self.y==0:
            raise ZeroDivisionError
        

