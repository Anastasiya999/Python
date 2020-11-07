def odwracanie_it(L, left, right):
    '''Odwraca kolejność elementów na liście od numeru left do right włącznie iteracyjnie'''
    while (right-left)>0:
        L[left], L[right] = L[right], L[left]
        left+=1
        right-=1
    return

def odwracanie_rek(L,left,right):
    '''Odwraca kolejność elementów na liście od numeru left do right włącznie rekurencyjnie'''
    if right-left<=0:return
    L[left], L[right] = L[right], L[left]
    odwracanie_rek(L,left+1,right-1)
    

L=list(range(10))
odwracanie_it(L,2,6)
assert L==[0,1,6,5,4,3,2,7,8,9]