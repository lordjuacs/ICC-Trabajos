aleato = [[3.4, 21, 3.0, 41, 2.8, 61, 3.4, 81, 3.2],
          [2, 2.9, 22, 4.1, 42, 4.0],
          [62, 3.4, 82, 3.6, 3, 2.8, 23, 4.2],
          [43, 3.6, 63, 3.4],
          [83, 3.8, 4]]

for i in range(5):
    aleato[i].append(max(aleato[i]))
    aleato[i].pop(0)
    cant = 0
    for valor in aleato[i]:
        if valor > 10:
            cant += 1
    print("Numeros mayores que 10 en la fila " + str(i) + " : ", cant)
print("Numeros aleatorios:")
for i in range(5):
    print(aleato[i])