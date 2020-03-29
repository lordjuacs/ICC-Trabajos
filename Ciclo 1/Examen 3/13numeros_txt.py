def insertion_sort_ascendente(lista):
    for i in range(1, len(lista)):
        h = i
        while h > 0 and lista[h] < lista[h - 1]:
            aux = lista[h]
            lista[h] = lista[h - 1]
            lista[h - 1] = aux
            h -= 1


numeros = []

input_file = open("numeros.txt", "r")
for cadena in input_file:
    (numero1, numero2) = cadena.split(" ")
    numero1 = int(numero1)
    numero2 = int(numero2)
    numeros.append(numero1)
    numeros.append(numero2)

input_file.close()
print("numeros antes =", numeros)
insertion_sort_ascendente(numeros)

print("numeros despues =", numeros)
