O = input()
E = input()


cont = True
i = 0
s = str()

while i < len(O):
    s += O[i]
    if cont == False:
        break
    s += E[i]
    if i == len(E)-1:
        cont = False
    i += 1
    
print(s)