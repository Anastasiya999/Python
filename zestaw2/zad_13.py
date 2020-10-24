# coding: utf-8 
line="\tLooking out my window\n\tIn October's golden light,\n\tI see a beauty unsurpassed,\n\tA truly lovely sight"
print(line)
print("Total sum:")

#pierwszy sposób
#print(len("".join(line.split())))

#drugi sposób
print(sum(len(x) for x in line.split()))
