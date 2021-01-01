# 10.2
import unittest

class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full(): raise ValueError("Stos jest pełny")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty(): raise ValueError("Stos jest pusty")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack_default = Stack()
        self.stack_3= Stack(3)
        self.sample = list(range(1,5))


    def testPush(self):
        self.stack_3.push(self.sample[0])
        self.stack_3.push(self.sample[1])
        self.assertEqual(self.stack_3.pop(),self.sample[1])

        self.stack_3.push(self.sample[1])
        self.stack_3.push(self.sample[2])
        self.assertRaises(ValueError, Stack.push, self.stack_3, self.sample[3])

        
    def testPop(self):

        self.assertRaises(ValueError, Stack.pop, self.stack_default)
        for i in range(10):
            self.stack_default.push(i)
        
        self.assertEqual(self.stack_default.pop(), 9)

    def testIsFull(self):
        self.assertFalse(self.stack_default.is_full())

    def testIsEmpty(self):
        self.assertTrue(self.stack_default.is_empty())
    
        
        
    def tearDown(self): pass
        
    
    

if __name__ == '__main__':
    unittest.main()
