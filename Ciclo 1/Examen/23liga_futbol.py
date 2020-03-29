EQUIPOS = ["Deportivo Municipal", "Alianza Lima", "Universidad Cesar Vallejo", "Universidad Tecnica de Cajamarca", "Deportivo Binacional", "Sporting Cristal"]
datos = [[13, 5, 5, 3], [13, 5, 4, 4], [13, 6, 2, 5], [13, 4, 7, 2], [14, 11, 0, 3], [13, 8, 4, 1]]
puntos = []
for i in range(len(datos)):
    victorias = datos[i][1] * 3
    puntaje = victorias + (datos[i][2])
    puntos.append(puntaje)
    print(EQUIPOS[i] + ": " + str(puntaje))
indice_mayor = puntos.index(max(puntos))
indice_menor = puntos.index(min(puntos))
print("El equipo con el mayor puntaje es: " + EQUIPOS[indice_mayor])
print("El equipo con el menor puntaje es: " + EQUIPOS[indice_menor])