line="\tLooking out my window\n\tIn October's golden light,\n\tI see a beauty unsurpassed,\n\tA truly lovely sight"

list_line=line.split()
list_line.sort(key=len,reverse=True)
print("the longest expression: \""+list_line[0]+"\", which length="+str(len(list_line[0])))