import unittest
from triangles import *


class TestTriangle(unittest.TestCase): 
     

    def setUp(self):
       self.tr1=Triangle(-2,0,0,4,3,0)
       self.tr2=Triangle(2,0,0,-4,-3,0)
       self.center_tr1=Point((-2+0+3)/3,(0+4+0)/3)
       self.area_tr1=10

    def test_print(self):
       self.assertEqual(str(self.tr1),"[(-2.0, 0.0), (0.0, 4.0), (3.0, 0.0)]")
       self.assertEqual(repr(self.tr1),"Triangle(-2.0, 0.0, 0.0, 4.0, 3.0, 0.0)")

    def test_cmp(self):
        self.assertTrue(self.tr1==self.tr1)
        self.assertFalse(self.tr1==self.tr2)

        self.assertTrue(self.tr1!=self.tr2)
        self.assertFalse(self.tr1!=self.tr1)

        
    def test_center(self):
        self.assertEqual(self.tr1.center(),self.center_tr1 )
        self.assertNotEqual(self.tr2.center(),self.center_tr1)
        

    def test_area(self):
        self.assertEqual(self.tr1.area(),self.area_tr1)
        self.assertTrue(self.tr2.area()==self.area_tr1)
       
       
    def test_move(self):
        self.assertEqual(self.tr1.move(2,2),Triangle(0,2,2,6,5,2))
        self.assertFalse(self.tr2.move(1,1)==self.tr2)
     
    def test_make4(self):
        self.assertEqual(set(self.tr1.make4()),set((Triangle(-2.0, 0.0, -1.0, 2.0, 0.5, 0.0),  Triangle(-1.0, 2.0, 0.0, 4.0, 1.5, 2.0), Triangle(-1.0, 2.0, 0.5, 0.0, 1.5, 2.0),Triangle(1.5, 2.0, 3.0, 0.0, 0.5, 0.0))) )

    def test_error(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 1, 4, 1, 5)
        with self.assertRaises(TypeError):
            Triangle("1", (1,), 2, 4, 1, 5 )


    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
