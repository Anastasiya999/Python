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

        self.assertEqual(5+self.zero,Frac(5,1))
        self.assertEqual(0.5+self.positive,Frac(5,4))
        self.assertEqual(self.zero+5, 5+self.zero)
        self.assertEqual(self.positive + 0.5, 0.5 + self.positive )

        self.assertRaises(TypeError,Frac.__add__, "hello",self.zero)
        self.assertRaises(TypeError,Frac.__radd__, self.positive,(1,2))
        

    def test_sub(self):
        self.assertEqual(Frac(1,2)-Frac(8,16),self.zero)
        self.assertNotEqual(self.zero-self.positive,self.positive)

        self.assertEqual(0 - self.positive, -self.positive)
        self.assertEqual(0.5 - Frac(1, 2), self.zero)
        self.assertEqual(self.positive - 0, self.positive)
        self.assertEqual(Frac(1, 4) - 0.25, self.zero)

        self.assertRaises(TypeError,Frac.__sub__, self.positive,[1,2])
        self.assertRaises(TypeError,Frac.__rsub__, {1:5},self.zero)


    def test_div(self):
        self.assertEqual(Frac(1,2) / Frac(1,2), Frac(1,1))
        self.assertNotEqual(self.zero / self.positive, self.positive)

        self.assertEqual(self.positive / 2, Frac(3,8))
        self.assertEqual(self.zero / 1.2, self.zero)
        self.assertEqual(0.5 / Frac(1,2), Frac(1, 1))
        self.assertEqual(2 / self.positive, Frac(8, 3))

        self.assertRaises(TypeError, Frac.__truediv__, self.positive, [3, 4])
        self.assertRaises(TypeError, Frac.__rtruediv__, self.positive, "3/5")
        self.assertRaises(ValueError, Frac.__truediv__,self.positive,self.zero)
        self.assertRaises(ValueError, Frac.__truediv__,self.positive, 0)
        self.assertRaises(ValueError, Frac.__rtruediv__, self.zero, 1.5)
        
    def test_floor_div(self):
        self.assertEqual(Frac(1, 2) // Frac(1, 2), Frac(1, 1))
        self.assertEqual(self.positive // Frac(1, 2), Frac(1, 1))

        self.assertEqual(self.negative // self.positive, Frac(-1, 1))
        self.assertEqual(0.25 // self.positive, self.zero)
        self.assertEqual(1 // self.negative, Frac(-2, 1))

        self.assertRaises(TypeError, Frac.__floordiv__, self.positive, [3, 4])
        self.assertRaises(TypeError, Frac.__rfloordiv__, self.positive, "3/5")
        self.assertRaises(ValueError, Frac.__floordiv__, self.positive,self.zero )
        self.assertRaises(ValueError, Frac.__floordiv__, self.positive, 0)
        self.assertRaises(ValueError, Frac.__rfloordiv__, self.zero, 1.5)


    def test_mul(self):
        self.assertEqual(self.zero*self.positive,self.zero)
        self.assertNotEqual(Frac(2,5)*Frac(3,4),Frac(5,20))

        self.assertEqual(0 * self.positive, self.zero)
        self.assertEqual(0.25 * self.positive, Frac(3, 16))
        self.assertEqual(self.positive * 0, 0 * self.positive)
        self.assertEqual(self.negative * 0.5, Frac(-5, 14))
    
    def test_neg(self):
        self.assertEqual(-self.positive, Frac(-3, 4))

    def test_invert(self):
        self.assertEqual(~self.positive, Frac(self.positive.y, self.positive.x) )

    def test_float(self):
        self.assertEqual(float(Frac(1,2)),1/2)
        self.assertNotEqual(float(self.positive),3//4)
    
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
    

    