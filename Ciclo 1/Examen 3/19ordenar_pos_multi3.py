import random


def crear_lista(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(1,99))
    return lista


def insertion_sort_ascendente(lista):
    for i in range(0, len(lista), 3):
        h = i
        while h > 1 and lista[h] < lista[h - 3]:
            aux = lista[h]
            lista[h] = lista[h - 3]
            lista[h - 3] = aux
            h -= 3


n = int(input("Ingrese el numero: "))
li = crear_lista(n)
print("La lista original es:", li)
insertion_sort_ascendente(li)
print("La lista ordenada es:", li)