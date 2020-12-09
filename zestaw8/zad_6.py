#8.6

count = 0
class P:
    
    def __init__(self):
        self.cache = {(0, 0):0.0, (0, 1):1.0, (1, 0): 0.0}

    def __call__(self, i, j):
        """wersja dynamiczna"""
        global count
        if (i, j) in self.cache:
            count+=1
            return self.cache[(i, j)]
        if i>0 and j>0:
            count+=1
            self.cache[(i, j)] = 0.5 * (self(i - 1, j) + self(i, j - 1))
        elif i==0:
            count+=1
            return self.cache[(0,1)]
        else:
            count+=1
            return self.cache[(1,0)]
        
        return self.cache[(i, j)]


def rec(i, j):
    """wersja rekurencyjna"""
    global count
    if i == 0 and j == 0:
        count+=1
        return 0.5
    elif i > 0 and j == 0:
        count+=1
        return 0.0
    elif i == 0 and j > 0:
        count+=1
        return 1.0
    else:
        count+=1
        return 0.5 * (rec(i - 1, j) + rec(i, j - 1))    

p=P()
print(p(5,2)) 
print("Liczba operacji, wersja dynamiczna: ", count)
count = 0
print(rec(5, 2))
print("Liczba operacji, wersja rekurencyjna: ", count)      
