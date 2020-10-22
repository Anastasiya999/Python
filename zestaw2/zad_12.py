line="\tLooking out my window\n\tIn October's golden light,\n\tI see a beauty unsurpassed,\n\tA truly lovely sight"
line_list=line.split()
sentenceOfFirstChar=""
sentenceOfLastChar=""

for item in line_list:
    sentenceOfFirstChar+=item[0]
    sentenceOfLastChar+=item[-1]

print("the whole line:\n"+line)
print(line_list)
print("first sentence: "+sentenceOfFirstChar)
print("last sentence: "+sentenceOfLastChar)