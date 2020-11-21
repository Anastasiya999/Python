import unittest
from fracs import *

class TestFracs(unittest.TestCase):

    def setUp(self):
        self.zero=Frac(0,1)
        self.negative=Frac(-5,7)
        self.positive=Frac(3,4)
        self.need_simplify=Frac(5,10)

    def test_print(self):
        self.assertEqual(str(self.need_simplify),"1/2")
        self.assertEqual(repr(self.zero),"Frac(0, 1)")


    def test_cmp(self):

        self.assertTrue(self.positive==self.positive)
        self.assertFalse(self.positive==self.zero)
        self.assertTrue(self.need_simplify==Frac(1,2))

        self.assertTrue(self.positive!=self.negative)
        self.assertFalse(self.zero!=Frac(0,4))

        self.assertTrue(Frac(2,5)<Frac(3,5))
        self.assertFalse(Frac(-2,7)<Frac(-5,7))

        self.assertTrue(Frac(2,5)<=Frac(3,5))
        self.assertFalse(self.positive<=self.negative)

        self.assertTrue(self.positive>self.negative)
        self.assertFalse(self.zero>Frac(0,2))

        self.assertTrue(self.zero>=Frac(0,5))
        self.assertFalse(self.negative>=self.positive)

    def test_add(self):
        self.assertEqual(self.zero+Frac(5,6),Frac(5,6))
        self.assertNotEqual(Frac(-5,8)+Frac(4,8), self.zero)

    def test_sub(self):
        self.assertEqual(Frac(1,2)-Frac(8,16),self.zero)
        self.assertNotEqual(self.zero-self.positive,self.positive)

    def test_div(self):
        self.assertEqual(Frac(1,2)/Frac(1,2),Frac(1,1))
        self.assertNotEqual(self.zero/self.positive,self.positive)
        self.assertRaises(ZeroDivisionError,Frac.__truediv__,self.positive,self.zero)
        
    def test_mul(self):
        self.assertEqual(self.zero*self.positive,self.zero)
        self.assertNotEqual(Frac(2,5)*Frac(3,4),Frac(5,20))

    def test_float(self):
        self.assertEqual(float(Frac(1,2)),1/2)
        self.assertNotEqual(float(self.positive),3//4)
    
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
    

    