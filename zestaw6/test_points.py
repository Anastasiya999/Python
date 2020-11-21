import unittest
import math
from points import *

class TestPoint(unittest.TestCase): 
    def setUp(self):
        self.point1=Point(1,2)
        self.point2=Point(-5,2)
        self.zero=Point(0,0)
        

    def test_print(self):
        self.assertEqual(str(self.point1), "(1, 2)")
        self.assertEqual(repr(self.zero),"Point(0, 0)")
        self.assertNotEqual(str(self.point2),repr(self.point2))
       

    def test_cmp(self):
        self.assertTrue(self.point1==self.point1)
        self.assertFalse(self.point1==self.point2)

        self.assertTrue(self.zero!=self.point1)
        self.assertFalse(self.zero!=self.zero)

    def test_add(self):
        self.assertEqual(self.point1+self.point2, Point(-4,4))
        self.assertNotEqual(self.zero+self.point2, self.point1)

    def test_sub(self):
        self.assertEqual(self.point1-self.point1, self.zero)
        self.assertNotEqual(self.zero-self.point1,self.point1)
        
    def test_mul(self):
        self.assertEqual(self.point1*self.point1,Point(1,4))
        self.assertNotEqual(self.point1*self.zero, self.point1)

    def test_cross(self):
        self.assertEqual(self.point1.cross(self.point2), 12)
        self.assertNotEqual(self.point1.cross(self.zero), 1)

    def test_length(self):
        self.assertEqual(self.point1.length(),math.sqrt(5))
        self.assertNotEqual(self.zero.length(),2)
    
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
    

    