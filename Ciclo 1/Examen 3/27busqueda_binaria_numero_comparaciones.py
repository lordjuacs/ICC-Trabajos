def busquedaBinaria(Lista, item):
    low = 0
    high = len(Lista) - 1
    comparacion = 0
    encontrado = False
    while (low <= high) and not encontrado:
        mid = low + (high - low) // 2
        if Lista[mid] == item:
            comparacion += 1
            encontrado = True
        else:
            if item < Lista[mid]:
                high = mid - 1
                comparacion += 1
            else:
                low = mid + 1
                comparacion += 1
    return (encontrado, comparacion)


lista = [10,20,30,40,50,60,70,80,90]
buscar = int(input("Ingrese numero a buscar: "))
(si_o_no, compa) = busquedaBinaria(lista, buscar)

if si_o_no == True:
    print("El numero " + str(buscar) + " se encuentra en la lista despues de " + str(compa) + " comparaciones")

else:
    print("El numero " + str(buscar) + " no se encuentra en la lista despues de " + str(compa) + " comparaciones")
