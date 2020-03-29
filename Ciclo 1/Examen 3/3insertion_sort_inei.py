def insertion_sort_descendente(lista):
    for i in range(1, len(lista)):
        h = i
        while h > 0 and lista[h] > lista[h - 1]:
            aux = lista[h]
            lista[h] = lista[h - 1]
            lista[h - 1] = aux
            h -= 1


def ordenar_poblacion(dic):
    lista = list(dic.values())
    insertion_sort_descendente(lista)
    return lista


inei = {"Molina": 175237, "Callao": 426649, "Victoria": 174958,
        "Comas": 532403, "Agustino": 194474, "Carabayllo": 305963,
        "Olivos": 377532, "Cieneguilla": 47860, "Lince": 51054,
        "Independencia": 220654, "Jesus Maria": 73439, "Ate": 638345,
        "Carmen Legua": 43156, "Mi Peru": 52722, "Ventanilla ": 356040,
        "Lima": 276861, "Ancon": 43951, "Barranco": 30698, "Bellavista": 78489,
        "La Perla": 64111, "Brena": 77291, "Chaclacayo": 44271, "Chorrillos": 330483}

ordenada = ordenar_poblacion(inei)
mayor_poblacion = ordenada[0]
menor_poblacion = ordenada[len(ordenada) - 1]

print("Poblacion ordenada:", ordenada)
print("Poblacion mas alta:", mayor_poblacion)
print("Poblacion mas baja:", menor_poblacion)