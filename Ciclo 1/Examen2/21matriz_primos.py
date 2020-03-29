primos = [[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41],
          [43, 47, 53, 59, 61, 67, 71],
          [73, 79, 83, 89, 97, 101, 103, 107, 109, 113],
          [127, 131, 137, 139, 149, 151, 157]]
cant = 0
for i in range(len(primos)):
    primos[i].pop(1)
    primos[i].pop(-1)
    primos[i].append(min(primos[i]))
    for valor in primos[i]:
        if valor in range(50, 101):
            cant += 1
print("La cantidad es:", cant)
print("Numeros Primos: ")
for i in range(len(primos)):
    print(primos[i])