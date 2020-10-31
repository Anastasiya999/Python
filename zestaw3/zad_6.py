x=2   #wiersze
y=4   #kolumny
napis=""
for i in range(x+3):
        if i%2==0:
            wyraz="---".join("+" for j in range(y+1))+"\n"
        else:
            wyraz="   ".join("|" for i in range(y+1))+"\n"
        napis+=wyraz
print(napis)