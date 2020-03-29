def lista_tuplas(Lista):
    lista_tuplas = []
    letras_usadas = []
    for i in Lista:
        if i not in letras_usadas:
            letras_usadas.append(i)
            tupla = (Lista.count(i), i)
            lista_tuplas.append(tupla)
    return lista_tuplas



def insertion_sort_descendente(lista):
    for i in range(1, len(lista)):
        h = i
        while h > 0 and lista[h][0] > lista[h - 1][0]:
            aux = lista[h]
            lista[h] = lista[h - 1]
            lista[h - 1] = aux
            h -= 1
    return lista[:3]

def insertion_sort_ascendente(lista):
    for i in range(1, len(lista)):
        h = i
        while h > 0 and lista[h][1] < lista[h - 1][1] and lista[h][0] < lista[h - 1][0]:
            aux = lista[h]
            lista[h] = lista[h - 1]
            lista[h - 1] = aux
            h -= 1
    return lista



entrada = list(input().lower())
if 3 < len(entrada) <= 10000:
    tuplas_lista = lista_tuplas(entrada)
    ordenada = insertion_sort_descendente(tuplas_lista)
    maybe = insertion_sort_descendente(ordenada)
    for i in range(3):
        print(maybe[i][1], maybe[i][0])
