N = int(input())
lista = []
suma = 0
for i in range(N):
    tiempo = float(input())
    lista.append(tiempo)
    suma += tiempo
lista.sort()
promedio = suma / N
index_max = lista.index(max(lista))
for _ in lista:
    print(_,end=" ")
print()
print(promedio)
print(lista[index_max - 1])
print(max(lista))
