def insertion_sort_ascendente(lista):
    cont = 0
    for i in range(1, len(lista)):
        h = i
        while h > 0 and lista[h] < lista[h - 1]:
            aux = lista[h]
            lista[h] = lista[h - 1]
            lista[h] = lista[h - 1]
            lista[h - 1] = aux
            h -= 1
            cont += 1
    return (lista, cont)


lista = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
(nueva, veces) = insertion_sort_ascendente(lista)

print("Lista ordenada de manera ascendente:", nueva)
print("Total de movimientos realizados:", veces)