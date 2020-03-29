def partition_left_pivot(A, low, high):
    i = low
    pivot = A[low]
    for j in range(low + 1, high + 1):
        if A[j] <= pivot:
            i += 1
            if i != j:
                A[i], A[j] = A[j], A[i]
    A[i], A[low] = A[low], A[i]
    posicion = i
    return posicion

def quicksort(A, low, high):
    if low < high:
        posicion = partition_left_pivot(A, low, high)
        quicksort(A, low, posicion - 1)
        quicksort(A, posicion + 1, high)


lista = input().split(" ")

lista = [int(i) for i in lista]
print("test =", lista)
quicksort(lista, 0, len(lista) - 1)
print("ordenada =", lista)
segundo_mayor = lista[-2]
print("segundo_mayor =", segundo_mayor)

