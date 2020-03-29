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
    if encontrado == True:
        return (encontrado, mid)
    else:
        return (encontrado, encontrado)


lista = [i for i in range(7, 498, 7)]
buscar = int(input("Ingrese numero a buscar: "))
(si_o_no, posicion) = busquedaBinaria(lista, buscar)

if si_o_no == True:
    print("El numero esta esta en la posicion " + str(posicion) + " de la lista")
else:
    print("El numero NO esta en la lista")