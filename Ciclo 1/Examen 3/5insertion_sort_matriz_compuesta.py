def insertion_sort_ascendente(lista):
    for i in range(1, len(lista)):
        h = i
        while h > 0 and lista[h] < lista[h - 1]:
            aux = lista[h]
            lista[h] = lista[h - 1]
            lista[h - 1] = aux
            h -= 1

def ordenar_matriz(matrizcompues):
    size = len(matrizcompues)
    for i in range(size):
        insertion_sort_ascendente(matrizcompues[i])
    return matrizcompues


compues = [[8, 9, 14, 15, 16, 18, 4, 6, 10, 12],
           [21, 22, 25, 26, 27, 20, 24],
           [34, 28, 32, 33, 30], [38, 39, 42, 44, 35, 36, 40],
           [52, 54, 45, 48, 49, 50, 51, 46]]

nueva = ordenar_matriz(compues)

for i in nueva:
    print(i)

for i in range(len(nueva)):
    print(nueva[i][len(nueva[i]) - 1])

