def busquedaBinaria(Lista, item):
    low = 0
    high = len(Lista) - 1
    encontrado = False
    while (low <= high) and not encontrado:
        mid = low + (high - low) // 2
        if Lista[mid] == item:
            encontrado = True
        else:
            if item < Lista[mid]:
                high = mid -1
            else:
                low = mid + 1
    return (encontrado, mid)


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


lista = []
while True:
    n = int(input("Ingrese un numero entero: "))
    if n >= 5:
        break

for i in range(n):
    numero = int(input())
    lista.append(numero)

quicksort_left(lista, 0, len(lista) - 1)
print("Lista:", lista)
buscar = int(input("Ingrese numero a buscar: "))
(si_o_no, posicion) = busquedaBinaria(lista, buscar)
if si_o_no == True:
    print("Se encontro", buscar, "en la posicion", posicion)
else:
    li = [0 for i in range(len(lista))]
    print("No se encontro " + str(buscar) + ". -->", li)