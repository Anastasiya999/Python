# coding: utf-8
line="\tLooking out my window\n\tIn October's golden light,\n\tI see a beauty unsurpassed,\n\tA truly lovely sight"
print("Expressions to sort: "+str(line.split()))
print("Sorted\n\tAlfabetically: "+str(sorted(line.split())))
print("\tBased on length:"+str(sorted(line.split(),key=len)) )