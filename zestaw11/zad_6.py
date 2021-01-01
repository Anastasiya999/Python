# 11
from stack import *
from zad_1 import get_random_numbers

def quicksort_iterative(array):
    left = 0
    right = len(array)-1
    stack = Stack(len(array))
    stack.push((left, right))

    while not stack.is_empty():
        left, right = stack.pop()
        pivot = partition(array, left, right)
        if pivot - 1 > left:
            stack.push((left, pivot - 1))

        if pivot + 1 < right:
            stack.push((pivot + 1, right))
 

def partition(array, left, right):
    pivot = array[right]
    i = left
    for j in range (left, right):
        if array[j] <= pivot:
           swap(array, i, j)
           i += 1
    swap(array, i, right)
    return i

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

if __name__ == '__main__':
 
    array = get_random_numbers(10)
    print('before sorting: ', array)
    quicksort_iterative(array)
    print('after: ',array)

    
    

