n = int(input("Tamano: "))
matriz = []
for i in range(n):
    fila = input("Fila " + str(i) + ": ").split(" ")
    matriz.append(fila)
pos_i = int(input("Posicion i: "))
pos_j = int(input("Posicion j: "))
resultado = matriz[pos_i][pos_j]
print("Resultado:", resultado)
