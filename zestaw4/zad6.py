def sum_seq(sequence):
    '''Oblicza sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje'''
    result=0
    for item in sequence:
        if isinstance(item,(list,tuple)):
           result+=sum_seq(item)
        else:
            result+=item
    return result
        
L=[1,2,3,[4,5,6],6,[11,0,5],8]       
print(sum_seq(L))