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

def partition_right_pivot(A, low, high):
    i = low
    pivot = A[high]
    for j in range(low, high):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[high] = A[high], A[i]
    posicion = i
    return posicion


def quicksort_left(A, low, high):
    if low < high:
        posicion = partition_left_pivot(A, low, high)
        quicksort_left(A, low, posicion - 1)
        quicksort_left(A, posicion + 1, high)

def quicksort_right(A, low, high):
    if low < high:
        posicion = partition_right_pivot(A, low, high)
        quicksort_right(A, low, posicion - 1)
        quicksort_right(A, posicion + 1, high)





#quicksort con pivot en el medio
def partition_pivot_medio(A, left, right):
    middle = (left + right) // 2
    pivot = A[middle]
    while left <= right:
        # encontrar el elemento en la izquierda que debe
        # estar en la derecha
        while A[left] < pivot:
            left += 1
        # encontrar el elemento en la derecha que debe
        # estar en la izquierda
        while A[right] > pivot:
            right -= 1

        # intecambiar elementos, mover left y right indeces
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
    posicion = left
    return posicion

def quicksort_middle(A, left, right):
    index = partition_pivot_medio(A, left, right)
    # ordenar en la mitad izquierda
    if left < index - 1:
        quicksort_middle(A, left, index - 1)

    # ordenar en la mitad derecha
    if index < right:
        quicksort_middle(A, index, right)

array = [1,5,2,131,11341,134,1,1414,14,14,41,4,1,1]
quicksort_middle(array, 0, len(array) - 1)
print(array)


