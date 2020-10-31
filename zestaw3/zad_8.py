seq1=list(range(1,7))+list(range(2,10,2))
print(seq1)

seq2=list(range(2,7))+list(range(3,10,3))
print(seq2)

#a)
print("Elementy wspólne: "+str(set(seq1).intersection(set(seq2))))

#b)
print("Suma elementów: "+str(set(seq1).union(set(seq2))))