def insertion_sort_descendente(lista):
    for i in range(1, len(lista)):
        h = i
        while h > 0 and lista[h] > lista[h - 1]:
            aux = lista[h]
            lista[h] = lista[h - 1]
            lista[h - 1] = aux
            h -= 1


def construir_diccionario(lista):
    dic = {}
    for i in range(1, len(lista) + 1):
        dic["Fila " + str(i)] = lista[-i]
    return dic


li= []
cont = 1
while True:
    altura = int(input("Altura " + str(cont) + ": "))
    if altura in range(50, 201):
        li.append(altura)
        cont += 1
        if len(li) == 5:
            break

insertion_sort_descendente(li)

diccionario = construir_diccionario(li)
print("Resultado:", diccionario)
