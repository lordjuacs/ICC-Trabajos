matriz = [[12, 4, 7, 1], [14, 3, 11, 6], [4, 12, 10, 8], [8, 2, 5, 2]]
columna_elegida = int(input())
operando = int(input())
nueva = []
if operando >= 1 and operando <= 15:
    for x in range(4):
        matriz[columna_elegida][x] = matriz[columna_elegida][x] * operando
        print(matriz[columna_elegida][x])