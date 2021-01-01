# 10.8

import unittest
import random

class RandomQueue:

    def __init__(self):
        self.items = []
        self.st = random.getstate()

    def __str__(self):
        return str(self.items)

    def insert(self, item):
        if self.is_full():
            raise ValueError("Kolejka pełna.")
        self.items.append(item)


    def remove(self):    # zwraca losowy element
        if self.is_empty():
            raise ValueError("Kolejka pusta")
        random.setstate(self.st)
        index = random.randint(0, len(self.items)-1)
        self.__swap(index, -1)
        return self.items.pop()


    def is_empty(self):
        return not self.items


    def is_full(self):
        return False

    def clear(self):     # czyszczenie listy
        self.items = []

    def __swap(self,indx_1,indx_2):
        self.items[indx_1], self.items[indx_2] = self.items[indx_2], self.items[indx_1]

class TestRandomQueue(unittest.TestCase):
    def setUp(self):
       self.queue = RandomQueue()
       self.queue_not_empty = RandomQueue()
       for i in range(5):
            self.queue_not_empty.insert(i)

    def testInsert(self):
        for i in range(10):
            self.queue.insert(i)
        self.assertEqual(str(self.queue), str(list(range(10))))

    def testRemove(self):
        for i in range(5):
            print(self.queue_not_empty.remove())

    
    def tearDown(self): pass
        
    
    

if __name__ == '__main__':
    unittest.main()


