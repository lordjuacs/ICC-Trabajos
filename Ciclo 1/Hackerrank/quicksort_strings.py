def partition(A, low, high ):
    i = low
#Elegimos el primer elemento del array como pivot
    pivot = A[low]
    for j in range( low + 1, high + 1):
        if A[j] <= pivot:
            i = i + 1
            if i != j:
                A[i], A[j] = A[j], A[i]
    A[i], A[low] = A[low], A[i]
    w = i
    return w


def quicksort(A, low, high):
    if low < high:
        w = partition(A, low, high)
        quicksort(A, low, w - 1)
        quicksort(A, w + 1, high)


dic = {' ': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
       'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}


tamano = int(input())
entrada = ""

for i in range(tamano):
    efe = input()
    entrada += efe + " "



entrada = list(entrada)
lista_entrada = []
for i in entrada:
    for e in dic:
        if i == e:
            lista_entrada.append(dic[e])

quicksort(lista_entrada, 0, len(lista_entrada) - 1)

for i in range(len(lista_entrada)):
    for e in dic:
        if dic[e] == lista_entrada[i]:
            lista_entrada[i] = e


