def partition_right_pivot(A, low, high):
    i = low
    pivot = A[high]
    for j in range(low, high):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[high] = A[high], A[i]
    posicion = i
    A.append(posicion)
    return A


n = int(input())
listaa = input().split(" ")
lista_enteros = [int(i) for i in listaa]
efe = partition_right_pivot(lista_enteros, 0, n - 1)
indice = efe[-1]
print(indice)
efe.pop(-1)
for i in range(len(efe)):
    print(efe[i], end=" ")