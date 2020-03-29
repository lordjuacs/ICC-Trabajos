def conteo_vecinos(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(1, filas - 1):
        for j in range(1, columnas - 1):
            if matriz[i][j] == matriz[i+1][j] and matriz[i][j] == matriz[i-1][j] and matriz[i][j] == matriz[i][j+1] and matriz[i][j] == matriz[i][j-1]:
                print("Matriz [" + str(i) + "][" + str(j) + "]:", matriz[i][j])

matriz = []
filas = int(input("filas: "))
columnas = int(input("columnas: "))
for i in range(filas):
    fila = input().split(" ")
    matriz.append(fila)

conteo_vecinos(matriz)