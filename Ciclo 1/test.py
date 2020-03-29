def conteo_vecinos(matriz):
    nueva = [[], [], []]
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            if i != 0 and i != filas - 1 and j != 0 and j != columnas - 1:
                if matriz[i][j] == matriz[i+1][j] and matriz[i][j] == matriz[i-1][j] and matriz[i][j] == matriz[i][j+1] and matriz[i][j] == matriz[i][j-1]:
                    nueva[0].append(matriz[i-1][j - 1])
                    nueva[0].append(matriz[i - 1][j])
                    nueva[0].append(matriz[i - 1][j + 1])
                    nueva[1].append(matriz[i][j - 1])
                    nueva[1].append(matriz[i][j])
                    nueva[1].append(matriz[i][j + 1])
                    nueva[2].append(matriz[i+1][j - 1])
                    nueva[2].append(matriz[i+1][j])
                    nueva[2].append(matriz[i+1][j + 1])
    return nueva
matriz = []
(filas, columnas) = input().split(" ")
filas = int(filas)
columnas = int(columnas)
for i in range(filas):
    fila = input().split(" ")
    matriz.append(fila)

nuevecita = conteo_vecinos(matriz)
for i in range(len(nuevecita)):
    for j in range(len(nuevecita[0])):
        print(nuevecita[i][j], end=" ")
    print()