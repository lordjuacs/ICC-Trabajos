a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
matriz = []
for i in range(1, a + 1):
    fila = []
    for j in range(1, a + 1):
        fila.append((b + i) * (c + j))
    matriz.append(fila)
for i in range(a):
    print(matriz[i])