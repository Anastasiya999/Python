#x = 2; y = 3;        zbędny drugi średnik
#if (x > y):
#    result = x;      zbędny średnik
#else:
#    result = y;      zbędny średnik
#-------------------------------------------------------prawidłowy zapis-----------------------------------
x = 2; y = 3
if (x > y):
    result = x
else:
    result = y
assert result==3

#for i in "qwerty": if ord(i) < 100: print (i)     niepoprawna składnia, wyrażenie if powinno stać z nowej linii po wcięciu
#-------------------------------------------------------prawidłowy zapis-----------------------------------
for i in "qwerty": 
    if ord(i) < 100: 
        print (i)

#for i in "axby": print (ord(i) if ord(i) < 100 else i)  niepoprawna składnia, wyrażenie print powinno stać z nowej linii po wcięciu
#-------------------------------------------------------prawidłowy zapis-----------------------------------
for i in "axby": 
    print (ord(i) if ord(i) < 100 else i)