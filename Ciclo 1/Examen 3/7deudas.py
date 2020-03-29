def ordenarDeudas_tuplas(lista):
    for i in range(1, len(lista)):
        h = i
        while h > 0 and lista[h][1] > lista[h - 1][1]:
            aux = lista[h]
            lista[h] = lista[h - 1]
            lista[h] = lista[h - 1]
            lista[h - 1] = aux
            h -= 1
    return lista

deudas =[("luz", 115), ("agua", 50), ("banco" , 3000), ("colegio", 850)]

print("Deudas ordenadas:", ordenarDeudas_tuplas(deudas))