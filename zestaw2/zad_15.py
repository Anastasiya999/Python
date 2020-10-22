L=[x for x in range(1,10)]
#pierwszy sposób
napis=""
for item in L:
    napis+=str(item)
#drugi sposób
expression="".join([str(x) for x in L])
print(L)
print(napis)
print(expression)