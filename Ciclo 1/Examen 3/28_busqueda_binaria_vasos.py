def busquedaBinaria(Lista, item):
    low = 0
    high = len(Lista) - 1
    encontrado = False
    while (low <= high) and not encontrado:
        mid = low + (high - low) // 2
        if Lista[mid] == item:
            encontrado = True
        else:
            if item > Lista[mid]:
                high = mid -1
            else:
                low = mid + 1
    if encontrado == True:
        return (encontrado, mid)
    else:
        return (encontrado, encontrado)

bolitas = [21 ,18 ,15 ,11 ,9 ,8 ,5 ,2]
buscar = 5
conteo = busquedaBinaria(bolitas, buscar)
print (" Vasos levantados :", conteo )