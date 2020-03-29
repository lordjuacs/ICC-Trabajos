(filas, columnas) = input().split(" ")
filas = int(filas)
columnas = int(columnas)
mayor = max(filas, columnas)
matriz = []
for i in range(filas):
    efe = input().split(" ")
    if "" in efe:
        efe.remove("")
    matriz.append(efe)

veces = int(input())

for i in range(filas):
    if matriz[i][-1] == "":
        matriz[i][-1] = " "

efe = len(matriz)

while True:
    if efe != mayor:
        matriz.append([])
        efe += 1
    if efe == mayor:
        break
cont = 0
while True:
    if len(matriz[cont]) != mayor:
        matriz[cont].append(" ")
    if len(matriz[cont]) == mayor:
        cont += 1
    if cont == len(matriz):
        break

import copy

cont = 0
while True:

    identica = copy.deepcopy(matriz)
    for i in range(mayor):
        for j in range(mayor):
            matriz[i][j] = identica[mayor - j - 1][i]
    cont += 1

    if cont == veces:
        break

nueva = []
for i in range(mayor):
    u = []
    for j in range(mayor):
        if matriz[i][j] not in ["", " "]:
            u.append(matriz[i][j])
    if u != []:
        nueva.append(u)

for i in range(len(nueva)):
    for j in range(len(nueva[0])):
        print(nueva[i][j], end=" ")
    print()
