def bubbleSort(listaTuplas):

    n = len(listaTuplas)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if listaTuplas[j] > listaTuplas[j + 1]:
                temp = listaTuplas[j]
                listaTuplas[j] = listaTuplas[j + 1]
                listaTuplas[j + 1] = temp

    ahora_si = []
    for i in range(len(listaTuplas)):
        ofo = (listaTuplas[i][1], listaTuplas[i][0])
        ahora_si.append(ofo)
    return ahora_si
# escriba aqui el algoritmo de ordenacion para una lista de tuplas


def juntarEdadDistancia(lista, Q):
    nueva_lista = []
    for i in lista:
        efe = (abs(Q - i), i)
        nueva_lista.append(efe)
    return nueva_lista

# escriba aqui el algoritmo para crear una nueva lista  de edades
# asociando la distancia de cada edad a Q


def K_VecinosCercanos(lista, Q, k):
    listaTuplas = juntarEdadDistancia(lista, Q)
    listaDist = bubbleSort(listaTuplas)
    return listaDist[:k]


# -----<lectura de datos y llamada a funciones>----
edadesStr = input("").split(",")
edadesInt = [int(i) for i in edadesStr]
Q = int(input(""))
k = int(input(""))
vecinos = K_VecinosCercanos(edadesInt, Q, k)

for e in vecinos:
    print(e)
