# 10.5

import unittest

class PriorityQueueP:

    def __init__(self):
        self.items = []

    def __str__(self):   # podglądamy kolejkę
        return str(self.items)


    def __len__(self):
        return len(self.items)


    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)
        self.__check_condition_up(self.items, len(self) - 1)

    def remove(self):
        #maxi = 0
        #for i in range(1, len(self.items)):
        #    if self.items[i] > self.items[maxi]:
        #        maxi = i
        #return self.items.pop(maxi)   # mało wydajne
        self.__swap(len(self) - 1, 0)
        max = self.items.pop()
        self.__check_condition_down(self.items, 0)
        return max
    


    def __check_condition_up( self, items, index):
        parent = self.__get_parent(index)

        if parent < 0:
            return 
        else:
            if items[index] > items[parent]:
                self.__swap( index, parent)
                self.__check_condition_up(items, parent)

    def __get_parent(self, index):
        return (index - 1)//2

    
    def __get_left_child(self, index):
        return 2 * index


    def __get_right_child(self, index):
        return 2 * index + 1

    def __swap(self, indx_1,indx_2):
        self.items[indx_1], self.items[indx_2] = self.items[indx_2], self.items[indx_1]

    def __check_condition_down(self, items, index):
        child = self.__get_left_child(index)
        if child >= len(items):
            return
        if child + 1 < len(items) and items[child] < items[child + 1]:
            child = child + 1
        if items[child] > items[index]:
            self.__swap(child, index)
            self.__check_condition_down(items, child)





class PriorityQueueT:

    def __init__(self, size=10):
        self.items = size * [None]
        self.n = 0   # pierwszy wolny indeks
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def insert(self, data):
        # brak zabezpieczenia
        if self.is_full(): raise ValueError("Kolejka pełna")
        self.items[self.n] = data
        self.n += 1

    def remove(self):
        # brak zabezpieczenia
        # Etap 1 - wyszukiwanie elementu.
        if self.is_empty(): raise ValueError("Kolejka pusta")
        maxi = 0
        for i in range(self.n):
            if self.items[i] > self.items[maxi]:
                maxi = i
        # Etap 2 - usuwanie elementu.
        self.n -= 1
        data = self.items[maxi]
        self.items[maxi] = self.items[self.n]
        self.items[self.n] = None   # usuwamy referencję
        return data   

class TestQueues(unittest.TestCase):
    def setUp(self):
        self.queueP = PriorityQueueP()
        self.queueT_empty = PriorityQueueT()
        self.queueT_full = PriorityQueueT(1)
        self.queueT_full.insert(10)
        for i in range(5):
            self.queueP.insert(i)

    def testRemoveP(self):
        self.assertEqual(self.queueP.remove(), 4)
        self.assertEqual(self.queueP.remove(), 3)
    

    def testRemoveT(self):
        self.assertRaises(ValueError, PriorityQueueT.remove, self.queueT_empty)

    def testInsertT(self):
        self.assertRaises(ValueError, PriorityQueueT.insert, self.queueT_full, 1)
    
    def tearDown(self): pass
        
    
    

if __name__ == '__main__':
    unittest.main()
