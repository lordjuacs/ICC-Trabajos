#quicksort con particion izquierda y derecha
# para variar ascendente y descendente solo se cambia > por <


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


def quicksort_left(A, low, high):
    if low < high:
        posicion = partition_left_pivot(A, low, high)
        quicksort_left(A, low, posicion - 1)
        quicksort_left(A, posicion + 1, high)


def ordenar_dos_listas(a, b):
    nueva = a + b
    quicksort_left(nueva, 0, len(nueva) - 1)
    return nueva


a = [9, 10, 3, 4]
b = [8, 5, 6, 7, 2, 1]

efe = ordenar_dos_listas(a, b)
print(efe)
