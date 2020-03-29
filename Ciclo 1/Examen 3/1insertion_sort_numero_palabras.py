def insertion_sort_ascendente(lista):
    for i in range(1, len(lista)):
        h = i
        while h > 0 and lista[h] < lista[h - 1]:
            aux = lista[h]
            lista[h] = lista[h - 1]
            lista[h - 1] = aux
            h -= 1


multiplos_5 = []
tres_letras = []

while True:
    numero = int(input("Ingrese numero : "))
    if numero == -1:
        break
    elif numero % 5 == 0:
        multiplos_5.append(numero)

print("---------------")
while True:
    palabra = input("Ingrese palabra: ")
    if palabra == "FIN":
        break
    if len(palabra) >= 3:
        tres_letras.append(palabra.upper())


insertion_sort_ascendente(multiplos_5)
for i in range(len(multiplos_5)):
    multiplos_5[i] = str(multiplos_5[i])

insertion_sort_ascendente(tres_letras)

print("Lista ordenada numeros (ascendente):", " ".join(multiplos_5))
print("Lista ordenada palabras (A-Z):", " ".join(tres_letras))