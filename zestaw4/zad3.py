from functools import reduce
def factorial(n):
    '''Iteracyjnie oblicza silnie od n'''
    i=1
    result=1
    if n==0 or n==1:
        return 1
    else:
        #pierwszy sposób
        while(i<=n):
            result=result*i
            i+=1
        return result
        # drugi sposób
        #return reduce(lambda x,y: x*y , range(1,n+1))

assert factorial(0)==1
assert factorial(3)==6
assert factorial(10)==3628800

