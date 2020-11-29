import math
class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.check_zeroDiv(y)
        self.x = x
        self.y = y
        self.simplify()
             

    def __str__(self):        
        """zwraca "x/y" lub "x" dla y=1"""
        if self.y==1:
            return "{}".format(self.x)

        else:
            return "{}/{}".format(self.x,self.y)
           

    def __repr__(self):        
        """zwraca "Frac(x, y)"\\"""
        return "Frac({}, {})".format(self.x,self.y)

    # Python 2
    #def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Python 2.7 i Python 3
    def __eq__(self, other):
        """sprawdza frac1 == frac2"""
        return self.x==other.x and self.y==other.y

    def __ne__(self, other):
        """sprawdza frac1 != frac2"""
        return not self == other

    def __lt__(self, other):
        """sprawdza frac1 < frac2"""
        result = float(self-other)
        return result < 0
        

    def __le__(self, other):
        """sprawdza frac1 <= frac2 """
        result = float(self-other)
        return result <= 0

    #def __gt__(self, other): pass

    #def __ge__(self, other): pass

    def __add__(self, other): 
        """frac1 + frac2"""
        if isinstance(self,Frac) and isinstance(other, Frac):
            """frac2 = Frac()"""
            x=self.x*other.y+other.x*self.y
            y=self.y*other.y
            return Frac(x, y)
        elif isinstance(self,Frac) and isinstance(other, int):
            """frac2 = int"""
            x = self.x+other*self.y
            y = self.y
            return Frac(x, y)
        elif isinstance(self, Frac) and isinstance(other, float):
            """frac2 = float"""
            other = other.as_integer_ratio()
            x=self.x*other[1]+other[0]*self.y
            y=self.y*other[1]
            return Frac(x, y)
        else:
            raise TypeError("Podaleś niepoprawny typ")

    
    __radd__ = __add__


    def __sub__(self, other):  # frac1 - frac2
        """frac1 - frac2"""

        if isinstance(self,Frac) and isinstance(other, Frac):
            """frac2 = Frac()"""
            x=self.x*other.y-other.x*self.y
            y=self.y*other.y
            return Frac(x, y)
        elif isinstance(self,Frac) and isinstance(other, int):
            """frac2 = int"""
            x = self.x-other*self.y
            y = self.y
            return Frac(x, y)
        elif isinstance(self, Frac) and isinstance(other, float):
            """frac2 = float"""
            other = other.as_integer_ratio()
            x=self.x*other[1]-other[0]*self.y
            y=self.y*other[1]
            return Frac(x, y)
        else:
            raise TypeError("Podaleś niepoprawny typ")

    
    def __rsub__(self, other):
        """(int|float) - frac2"""
        if isinstance(other, float):
            """frac2 = float"""
            other = other.as_integer_ratio()
            x=other[0]*self.y-self.x*other[1]
            y=self.y*other[1]
            return Frac(x, y)
        elif isinstance(other, int):
            return Frac(self.y * other - self.x, self.y)
        else:
            raise TypeError("Podaleś niepoprawny typ")

    def __mul__(self, other):   
        """frac1 * frac2"""
        if isinstance(self,Frac) and isinstance(other, Frac):
            """frac2 = Frac()"""
            x=self.x*other.x
            y=self.y*other.y
            return Frac(x,y)
        elif isinstance(self,Frac) and isinstance(other, int):
            """frac2 = int"""
            x=self.x*other
            y=self.y
            return Frac(x, y)
        elif isinstance(self, Frac) and isinstance(other, float):
            """frac2 = float"""
            other = other.as_integer_ratio()
            x=self.x*other[0]
            y=self.y*other[1]
            return Frac(x, y)
        else:
            raise TypeError("Podaleś niepoprawny typ")
    

    __rmul__=__mul__


    def __truediv__(self, other):  # frac1 / frac2
        """ frac1 / frac2 """

        if isinstance(self,Frac) and isinstance(other, Frac):
            """frac2 = Frac()"""
            x = self.x * other.y
            y = self.y * other.x
            return Frac(x, y)
        elif isinstance(self,Frac) and isinstance(other, int):
            """frac2 = int"""
            x = self.x 
            y = self.y * other
            return Frac(x, y)
        elif isinstance(self, Frac) and isinstance(other, float):
            """frac2 = float"""
            other = other.as_integer_ratio()
            x = self.x * other[1]
            y = self.y * other[0]
            return Frac(x, y)
        else:
            raise TypeError("Podaleś niepoprawny typ")

       
    def __rtruediv__(self, other):
        """(int|float) / frac2"""

        if isinstance(other, float) or isinstance(other, int):
            """frac2 = float"""
            other = other.as_integer_ratio()
            return Frac(other[0], other[1]) / self
        else:
            
            raise TypeError("Podaleś niepoprawny typ")

        
    def __floordiv__(self, other):
        """ frac1 // frac2 """
       
        if isinstance(self,Frac) and isinstance(other, Frac):
            """frac2 = Frac()"""
            x = self.x * other.y
            y = self.y * other.x
            if y==0: raise ValueError("Nie można dzielić przez zero")
            return Frac(x // y)
        elif isinstance(self,Frac) and isinstance(other, int):
            """frac2 = int"""
            x = self.x 
            y = self.y * other
            if y==0: raise ValueError("Nie można dzielić przez zero")
            return Frac(x // y)
        elif isinstance(self, Frac) and isinstance(other, float):
            """frac2 = float"""
            other = other.as_integer_ratio()
            x = self.x * other[1]
            y = self.y * other[0]
            if y==0: raise ValueError("Nie można dzielić przez zero")
            return Frac(x // y)
        else:
            raise TypeError("Podaleś niepoprawny typ")

    def __rfloordiv__(self, other):
        """(int|float|frac1) // frac2"""
        if isinstance(other, float) or isinstance(other, int):
            """frac2 = float"""
            other = other.as_integer_ratio()
            return Frac(other[0], other[1]) // self
        else:
            
            raise TypeError("Podaleś niepoprawny typ")
        

    # operatory jednoargumentowe
    def __pos__(self):  
        """ +frac = (+1)*frac"""
        return self

    def __neg__(self):  
        """-frac = (-1)*frac"""
        return Frac(-self.x, self.y)

    def __invert__(self): 
        """odwrotnosc: ~frac"""
        return Frac(self.y, self.x)

    def __float__(self):       
        """konwercja float(frac)"""
        return float(self.x/self.y)

    def simplify(self):
        """skraca ilamek"""
        if self.y<0:
            self.x*=-1
            self.y*=-1
        a=math.gcd(self.x,self.y)
        self.x,self.y= self.x//a,self.y//a

    def is_zero(self):                # bool, typu [0, x]
        return self.x==0 and self.y!=0
    
    def check_zeroDiv(self,y):
        if y==0:
            raise ValueError("Mianownik nie może być zero")
        
