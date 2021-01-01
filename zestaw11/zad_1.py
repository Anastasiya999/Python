# 11.1

import random 
import math

def get_random_numbers(limit):
    numbers = []
    for i in range(limit):
        numbers.append(i)
    random.shuffle(numbers)
    return numbers

def get_half_sorted_numbers(limit):
    numbers = random.sample(list(range(limit)), limit-1)
    shell_sort(numbers, k = 1)
    return numbers


def get_reversed_half_sorted_numbers(limit):
    numbers = get_half_sorted_numbers(limit)
    numbers.reverse()
    return numbers


def get_gauss_random(N):
    numbers = []
    mu = 0
    sigma = 1
    for i in range(N):
        numbers.append(random.gauss(mu, sigma))
    return numbers


def get_repeating_random(N):
    k = math.isqrt(N)
    sample_list = list(range(k+1))
    return list(random.choice(sample_list) for i in range(N))
    

def shell_sort(array, k = 0):
    n = len(array)
    h = n//2
    left = 0
    right = n
    while h > k:
        for i in range(left + h, right):
            for j in range(i,left + h - 1, -h):
                if array[j - h]>array[j]:
                    swap(array, j-h, j)
        h = h//2


def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]





