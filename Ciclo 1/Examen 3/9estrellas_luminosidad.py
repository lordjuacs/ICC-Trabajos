def convertir_a_tupla_de2(lista):
    nueva = []
    for i in range(len(lista)):
        luminosidad = ((lista[i][1]) ** 2) * ((lista[i][2]) ** 4)
        tupla = (lista[i][0], luminosidad)
        nueva.append(tupla)
    return nueva


def insertion_sort_ascendente_tuplas(lista):
    for i in range(1, len(lista)):
        h = i
        while h > 0 and lista[h][1] < lista[h - 1][1]:
            aux = lista[h]
            lista[h] = lista[h - 1]
            lista[h] = lista[h - 1]
            lista[h - 1] = aux
            h -= 1
    return lista


datos_generales = [("UY-Scuti", 1.71, 3365), ("Canis Mayoris", 1.42, 3490),
                   ("KY Cyg", 1.42, 3500), ("Mu Cephei", 1.26, 3750),
                   ("S Persei", 1.20, 3000), ("VX Sagittarii", 1.12, 3000)]


previa = convertir_a_tupla_de2(datos_generales)
final = insertion_sort_ascendente_tuplas(previa)

print("Ordenado por luminosidad:")
for i in range(len(final)):
    if i == len(final) - 1:
        print(final[i][0], end="")
    else:
        print(final[i][0], end=" , ")