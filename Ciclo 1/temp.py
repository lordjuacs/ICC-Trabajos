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
        for i in range(len(A)):
            print(A[i], end=" ")
        print()
        quicksort(A, low, w - 1)
        quicksort(A, w + 1, high)


li = input().split(" ")
lista = [int(i) for i in li]

quicksort(lista, 0, len(lista) - 1)
