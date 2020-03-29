cad1 = []
cad2 = []
cad3 = []
subindices = []
sumaCadenas = []
for i in range(1,4):
    c = input("Ingrese cadena " + str(i) + ": " )
    if i == 1:
        for x in c:
            cad1.append(x)
    elif i == 2:
        for x in c:
            cad2.append(x)
    else:
        for x in c:
            cad3.append(x)
for i in range(1,7):
    n = input("Ingrese n" + str(i) + ": ")
    subindices.append(int(n))
    if i == 2:
        for i in range(subindices[0],subindices[1]):
            sumaCadenas.append(cad1[i])
    elif i == 4:
        for i in range(subindices[2],subindices[3]):
            sumaCadenas.append(cad2[i])
    elif i == 6:
        for i in range(subindices[4],subindices[5]):
            sumaCadenas.append(cad3[i])
print("".join(sumaCadenas))