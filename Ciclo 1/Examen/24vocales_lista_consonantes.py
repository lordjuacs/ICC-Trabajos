frase_1 = input("frase 1: ").split(" ")
frase_2 = input("frase 2: ").split(" ")
lista1 = []
lista2 = []
for i in frase_1:
    if i[0].upper() in ["A","E","I","O","U"]:
        lista1.append(i)
for i in frase_2:
    if i[0].upper() not in ["A","E","I","O","U"]:
        lista2.append(i)
print(lista1)
print(lista2)