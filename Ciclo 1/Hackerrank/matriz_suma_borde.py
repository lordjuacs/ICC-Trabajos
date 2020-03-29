dimensiones = input()
matriz = []
n_lista = dimensiones.split(" ")
WIDTH = int(n_lista[0])
HEIGHT = int(n_lista[1])
for i in range(HEIGHT):
    n = input()
    for x in range(WIDTH):
        fila = n.split(" ")
        fila[x] = int(fila[x])
    matriz.append(fila)
    fila = []
print(matriz)
print(len(matriz))
u = ""
nueva_matriz = matriz.copy()
suma = 0
for i in range(HEIGHT):
    row = nueva_matriz[i]
    if i == 0 or i == HEIGHT -1:
        for x in range(WIDTH):
            row[x] = str(row[x])
            suma += int(row[x])
        print(" ".join(row))
    elif i == (HEIGHT - 1 ) // 2:
        for x in range(WIDTH):
            if x == 0 or x == WIDTH -1 or x == (WIDTH -1) // 2:
                row[x] = str(row[x])
                suma += int(row[x])

            else:
                row[x] = " "
        print(" ".join(row))
    else:
        for x in range(WIDTH):
            if x == 0 or x == WIDTH - 1:
                row[x] = str(row[x])
                suma += int(row[x])
            else:
                row[x] = " "
        print(" ".join(row))
print(suma)

