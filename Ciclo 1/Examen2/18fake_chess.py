print("input:")
tamano = int(input())
matriz = []
for i in range(1, tamano + 1):
    fila = []
    for j in range(1, tamano + 1):
        if j % 2 == 0:
            fila.append("@")
        else:
            fila.append("*")
    matriz.append(fila)

print("output:")

for i in range(tamano):
    for j in range(tamano):
        print(matriz[i][j], end="  ")
    print()