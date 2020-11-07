def fibonacci(n):
    '''Iteracyjna wersja obliczająca n-ty wyraz ciągu Fibonacciego'''
    a, b = 0, 1
    #pierwszy sposób
    for x in range(1,n+1):
        a, b = a+b, a
    return a

assert fibonacci(14)==377