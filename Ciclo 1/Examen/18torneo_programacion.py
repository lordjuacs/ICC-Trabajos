Equipos = ["Hands", "Pae", "Choice", "Huatcher"]
Resultados = [[3, 1, 3, 2], [3, 2, 3, 2], [3, 3, 1, 2], [3, 3, 3, 3]]
totales = []
max = 0
suma_inno = 0
for i in range(len(Resultados)):
    totales.append(sum(Resultados[i]))
    if Resultados[i][1] > max:
        max = Resultados[i][1]
    suma_inno += Resultados[i][3]

print("Resultados totales =",totales)
print("Puntaje diseno alto = " + Equipos[max])
print("Promedio innovacion =",suma_inno / 4)
