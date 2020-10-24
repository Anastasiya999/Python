line="\tLooking out my window\n\tIn October's golden light,\n\tI see a beauty unsurpassed,\n\tA truly lovely sight"
line_list=line.split()
sentenceOfFirstChar=""
sentenceOfLastChar=""
#pierwszy sposób
for item in line_list:
    sentenceOfFirstChar+=item[0]
    sentenceOfLastChar+=item[-1]
#print("expression built from the first characters: "+sentenceOfFirstChar)
#print("expression built from the last characters: "+sentenceOfLastChar)

print("the whole line:\n"+line)
print(line_list) 

#drugi sposób
print("expression built from the first characters: "+"".join([x[-1:] for x in line.split()]))
print("expression built from the last characters: "+"".join([x[0:1] for x in line.split()]))


