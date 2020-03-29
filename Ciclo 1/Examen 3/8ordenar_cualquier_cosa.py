def insertion_sort_ascendente(lista):
    for i in range(1, len(lista)):
        h = i
        while h > 0 and lista[h] < lista[h - 1]:
            aux = lista[h]
            lista[h] = lista[h - 1]
            lista[h] = lista[h - 1]
            lista[h - 1] = aux
            h -= 1


numeros = [10, 30, 110, 110.2, 20, 50, 2, 900, 2, 13]
insertion_sort_ascendente(numeros)
print(numeros)