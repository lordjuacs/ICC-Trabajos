def convertir_transpuesta(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    nueva = []
    for i in range(columnas):
        row = []
        for j in range(filas):
            row.append(matriz[j][i])
        nueva.append(row)
    return nueva


def suma_matrices(matriz1, matriz2):
    matriz_suma = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)
        matriz_suma.append(fila)
    return matriz_suma


def resta_matrices(matriz1, matriz2):
    matriz_resta = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            resta = abs(matriz1[i][j] - matriz2[i][j])
            fila.append(resta)
        matriz_resta.append(fila)
    return matriz_resta


(filas, columnas) = input().split(" ")
filas = int(filas)
columnas = int(columnas)

matriz1 = []
matriz2 = []

for i in range(filas):
    fila1 = input().split(" ")
    fila1 = [int(i) for i in fila1]
    matriz1.append(fila1)

for i in range(filas):
    fila2 = input().split(" ")
    fila2 = [int(i) for i in fila2]
    matriz2.append(fila2)

nueva1 = convertir_transpuesta(matriz1)
nueva2 = convertir_transpuesta(matriz2)
suma = suma_matrices(nueva1, nueva2)
resta = resta_matrices(nueva1, nueva2)

for i in range(len(suma)):
    for j in range(len(suma[0])):
        print(suma[i][j], end=" ")
    print()

print("---")
for i in range(len(resta)):
    for j in range(len(resta[0])):
        print(resta[i][j], end=" ")
    print()