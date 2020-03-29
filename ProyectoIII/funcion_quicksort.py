# se crea una funcion quicksort con particion de pivot izquierdo,
# ordenando la lista de mayor a menor


def partition(arr,low,high):
    i = low
    pivot = arr[low]
    for j in range(low + 1, high + 1):
        if arr[j] >= pivot:
            i = i + 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[low] = arr[low], arr[i]
    w = i
    return w


def quickSort(arr,low,high):
    if low < high:
        w = partition(arr, low, high)
        quickSort(arr, low, w-1)
        quickSort(arr, w+1, high)