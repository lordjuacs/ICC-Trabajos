from random import randint
n = int(input("Ingrese el tamano: "))
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        valor = randint(ord('a'), ord('z'))
        fila.append(chr(valor))
    matriz.append(fila)
print("La matriz es:")
for i in range(n):
    for j in range(n):
        print(matriz[i][j], end=" ")
    print()
diagonal = ""
for i in range(n):
    diagonal += matriz[i][i-1+1]
print("El texto es: " + diagonal)