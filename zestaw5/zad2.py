import unittest
from fracs import *

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.negative=[-1,2]
        self.frac1=[3,7]
        self.frac2=[-8,11]
  
        

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac(self.frac1,self.frac2),[-23,77])
        self.assertFalse(add_frac(self.frac1, [-self.frac1[0],self.frac1[1]]))

    def test_sub_frac(self):
        self.assertEqual(sub_frac([2,5],[4,-7]),[34,35])
        self.assertNotEqual(sub_frac(self.zero,self.frac1),self.frac1)

    def test_mul_frac(self):
        self.assertEqual(mul_frac(self.frac1,self.frac2),[-24,77])
        self.assertFalse(mul_frac(self.zero, self.frac1))

    def test_div_frac(self):
        self.assertEqual(div_frac(self.frac1,self.frac2),[-33,56])
        self.assertRaises(ZeroDivisionError,div_frac,self.frac1,[3,0])

    def test_is_positive(self):
        self.assertFalse(is_positive(self.negative))

    def test_is_zero(self):
        self.assertTrue(is_zero(self.zero))
        self.assertFalse(is_zero(self.negative))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.frac1,self.frac2),1)
        self.assertEqual(cmp_frac([0,5],[0,2]),0)
        self.assertEqual(cmp_frac([2,5],[4,10]),0)
        self.assertEqual(cmp_frac(self.zero,self.frac1),-1)


    def test_frac2float(self):
        self.assertAlmostEqual(frac2float(self.frac1),0.4286,places=4)
        self.assertAlmostEqual(frac2float(self.frac2),-0.7272727)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy