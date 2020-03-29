filas = int(input("Ingrese numero de filas: "))
count = 0
ver = 1
print("\t" + " ".join("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
for x in range(filas):
    print(x+1,end="\t")
    for y in range(26):
        count += 1
        if count == ver ** 2 + 1:
            ver += 1
            print("X", end=" ")
        else:
            print("_", end=" ")
    print()
