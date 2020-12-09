#8.4
import math
import unittest

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    
    
    if a < (b + c) and b < (a + c) and c < (a + b):
        p = (a + b + c)/2
        return math.sqrt(p * (p-a) * (p-b) * (p-c))
    else:
        raise ValueError("Dane boki nie mogą utworzyć trójkąt!")


class TestHeron(unittest.TestCase):

    def setUp(self):
        self.correct = (5, 8, 11)
        self.wrong = (3, 8, 11)
    
    def testHeron(self):
        self.assertAlmostEqual(heron(*self.correct), 18.33030277982336)
    
    def testError(self):
        self.assertRaises(ValueError, heron, *self.wrong)
    
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()



