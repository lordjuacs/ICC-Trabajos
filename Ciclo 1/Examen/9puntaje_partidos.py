def puntaje(lista, ganado = 3, empate = 1):
    puntaje = 0
    for i in lista:
        if i == "G":
            puntaje += ganado
        elif i == "E":
            puntaje += empate
    return puntaje
ingrese = input("Ingrese los valores de su lista: ").split(" ")
print(puntaje(ingrese, 5 , 2))
print(puntaje(ingrese))
