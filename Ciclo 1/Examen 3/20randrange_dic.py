from random import randrange


def insertion_sort_ascendente(lista):
    for i in range(len(lista)):
        h = i
        while h > 0 and lista[h] < lista[h - 1]:
            aux = lista[h]
            lista[h] = lista[h - 1]
            lista[h - 1] = aux
            h -= 1


n = int(input("ingrese n: "))
m = int(input("ingrese m: "))
d = {}


for i in range(1, m + 1):
    lista = [randrange(1, n) for x in range(1, n + 1)]
    insertion_sort_ascendente(lista)
    d[i] = lista

print(d)
