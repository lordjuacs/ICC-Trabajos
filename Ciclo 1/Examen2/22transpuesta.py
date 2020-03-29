def cambiar__transpuesta(matriz):
    m = len(matriz)
    n = len(matriz[0])
    trans = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(matriz[j][i])
        trans.append(row)
    return trans

m = int(input("Ingrese M: "))
n = int(input("ingrese N: "))
matriz = []
for i in range(m):
    fila = input("Fila " + str(i) + ": ").split(" ")
    matriz.append(fila)
transpuesta = cambiar__transpuesta(matriz)
for i in range(len(transpuesta)):
    for j in range(len(transpuesta[0])):
        print(transpuesta[i][j], end=" ")
    print()