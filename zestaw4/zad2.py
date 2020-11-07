def miarka(n):
    '''Zwraca miarkę o dlugosci n'''
    miarka="....".join("|" for x in range(n+1))
    miarka=miarka+"\n"+"".join("{:5d}".format(x) for x in range(n+1)).lstrip()
    return miarka

def draw_rectangle(x,y):
    '''Zwraca prostokąt zbudowany z x*y pól'''
    napis=""
    for i in range(x+3):
        if i%2==0:
            wyraz="---".join("+" for j in range(y+1))+"\n"
        else:
            wyraz="   ".join("|" for i in range(y+1))+"\n"
        napis+=wyraz
    return napis

print(miarka(15))
print(draw_rectangle(2,4))

