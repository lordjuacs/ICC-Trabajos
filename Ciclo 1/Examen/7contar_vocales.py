ingresa = input("Ingresan: ").split(" ")
total = 0
for i in range(1,int(ingresa[0])+1):
    por_palabra = 0
    for x in ingresa[i]:
        if x.upper() in ["A","E","I","O","U"]:
            por_palabra += 1
    if por_palabra >= 3:
        total += 1

print("Resultado:", total)