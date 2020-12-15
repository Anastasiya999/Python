# 9.5
import unittest

class Node:
    """Klasa reprezentująca węzeł listy dwukierunkowej."""

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)





class CyclicList:
    """Lista cykliczna oparta na listę dwukierunkową"""

    def __init__(self):
        self.length = 0
        self.head = None   # łącze do dowolnego węzła listy

    def is_empty(self):
        return self.head is None

    def insert_head(self, node):
        tmp = self.head
        if tmp is None:
            "lista pusta"
            self.head = node
            self.head.next = self.head
            self.head.prev = self.head
            
        else:
            tail = tmp.prev
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = tail
            tail.next = self.head
        self.length +=1
    
    def count(self):
        return self.length 


    def insert_tail(self, node):
        tmp = self.head
        if self.head is None:
            self.insert_head(node)
        else:
           tail = self.head.prev
           self.head.prev = node
           tail.next = node
           node.prev = tail
           node.next = self.head
        self.length +=1
            



    def search(self, data):   # zwraca node lub None
        if self.head is None:
            return None
        elif self.head.data==data:
            return self.head
        else:
            tmp = self.head
            while(tmp.next.data!=data and tmp.next!=self.head):
                tmp = tmp.next
            if tmp.next is self.head:
                return None
            else:
                return tmp.next


    def remove(self, node):
        tmp = self.head
        if node is self.head and self.length==1:
            self.head = None
        elif node is self.head and self.length>1:
            tail = self.head.prev
            current = self.head.next
            tail.next = current
            current.prev = tail
            self.head = current
            tmp = None
            self.length -=1  
        else:
            while (tmp.next is not node) and tmp.next is not self.head:
                tmp = tmp.next
            if tmp.next is self.head:
                pass
            else:
                current = tmp.next
                tmp.next = tmp.next.next
                tmp.next.prev = tmp
                current = None
                self.length -=1        
                
    def merge(self, other):   # scalanie dwóch list cyklicznych w czasie O(1)
        tail = self.head.prev
        tail_other = other.head.prev

        tail.next = other.head
        other.head.prev = tail
        tail_other.next = self.head
        self.head.prev = tail_other


    def clear(self):     # czyszczenie listy
        self.head = None
    


class TestCyclicList(unittest.TestCase):

    def setUp(self):
        self.nodes = [Node(11), Node(22), Node(33), Node(44)]
        self.clist = CyclicList()
        self.clist2 = CyclicList()
    
    def test_insert_head(self):
        self.clist.insert_head(self.nodes[0])
        self.assertEqual(self.clist.head,self.nodes[0])
        self.clist.insert_head(self.nodes[2])
        self.assertNotEqual(self.clist.head,self.nodes[1])


    def test_insert_tail(self):
        self.clist.insert_tail(self.nodes[1])
        self.clist.insert_tail(self.nodes[2])
        self.assertEqual(self.clist.head.prev,self.nodes[2])
        
    
    def test_search(self):
        self.clist.insert_head(self.nodes[0])
        self.assertEqual(self.clist.search(11), self.nodes[0])
        self.clist.insert_tail(self.nodes[2])
        self.assertEqual(self.clist.search(33), self.nodes[2])

    def test_remove(self):
        self.clist.insert_head(self.nodes[1])
        self.assertEqual(self.clist.head, self.nodes[1])
        self.clist.remove(self.nodes[1])
        self.assertEqual(self.clist.head, None)

        self.clist.insert_head(self.nodes[2])
        self.clist.insert_tail(self.nodes[3])
        self.clist.remove(self.nodes[2])
        self.assertEqual(self.clist.head,self.nodes[3])

    def test_merge(self):
        self.clist.insert_head(self.nodes[0])
        self.clist.insert_tail(self.nodes[1])

        self.clist2.insert_head(self.nodes[2])
        self.clist2.insert_tail(self.nodes[3])

        self.clist.merge(self.clist2)
        self.assertEqual(self.clist.head, self.nodes[0])
        self.assertEqual(self.clist.head.prev, self.nodes[3])

    def tearDown(self): pass
        
    
    

if __name__ == '__main__':
    unittest.main()



