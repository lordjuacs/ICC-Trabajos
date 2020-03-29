def insertion_sort_descendente_tuplas(lista):
    for i in range(1, len(lista)):
        h = i
        while h > 0 and lista[h][1] > lista[h - 1][1]:
            aux = lista[h]
            lista[h] = lista[h - 1]
            lista[h] = lista[h - 1]
            lista[h - 1] = aux
            h -= 1



Productos = [("Tinder", 100), ("Gmail", 20), ("Glovo", 50)]


insertion_sort_descendente_tuplas(Productos)
for i in range(len(Productos)):
    if i == len(Productos) - 1:
        print(Productos[i][0], end="")
    else:
        print(Productos[i][0], end=" ")