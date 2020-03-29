def superior_o_inferior(matriz, filas, columnas):
    # la diagonal se obtiene con: matriz[i][i - 1 + 1]
    suma_superior = 0
    suma_inferior = 0
    for i in range(filas):
        for j in range(columnas):
            if j > i - 1 + 1:
                suma_superior += int(matriz[i][j])
            elif j < i - 1 + 1:
                suma_inferior += int(matriz[i][j])
    if suma_superior > suma_inferior:
        return 1
    elif suma_superior < suma_inferior:
        return -1
    else:
        return 0

tamano = int(input("Ingrese el tamano: "))
matriz = []
for i in range(tamano):
    fila = input("Fila " + str(i) + ": ").split(" ")
    matriz.append(fila)

respuesta = superior_o_inferior(matriz, len(matriz), len(matriz[0]))
print("Resultado:", respuesta)