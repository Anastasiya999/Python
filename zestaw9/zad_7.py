# 9.7
import unittest

class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)
    
    def insert(self, node):
        if node.data < self.data:   # mniejsze na lewo
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        elif node.data > self.data:   # większe lub równe na prawo
            if self.right:
                self.right.insert(node)
            else:
                self.right = node
        else:
            pass                      #w przypadku duplikatów, ignoruje
    
    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return None

    

def bst_max(top):
    if top is None:
        raise ValueError
    if top.right:
        return bst_max(top.right)
    else:
        return top

def bst_min(top):
    if top is None:
        raise ValueError
    if top.left:
        return bst_min(top.left)
    else:
        return top

class TestBST(unittest.TestCase):

    def setUp(self):
        self.top = None
        self.root = Node(50)
        self.root.insert(Node(61))
        self.root.insert(Node(21))
        self.root.insert(Node(25))
        self.root.insert(Node(70))
        self.root.insert(Node(5))
        self.root.insert(Node(6))

    def test_bst_min(self):
        self.assertEqual(bst_min(self.root).data,5)

    def test_bst_max(self):
        self.assertEqual(bst_max(self.root).data,70)

    def testError(self):
        self.assertRaises(ValueError, bst_max, self.top)
        self.assertRaises(ValueError, bst_min, self.top)
        

    def tearDown(self): pass
        
    
    

if __name__ == '__main__':
    unittest.main()


        