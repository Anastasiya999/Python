L=[1, 20, 500, 4, 10, 150]
expression=""+" ".join([str(x).zfill(3) for x in L])
print("Initial list: "+str(L))
print("Processed: "+expression)