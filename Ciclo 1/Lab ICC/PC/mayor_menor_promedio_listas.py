a = int(input("Ingrese cantidad de numeros: "))
lista = []
suma = 0
cont = 1
for i in range(a):
    i = int(input("Ingrese numero " + str(cont) + ": "))
    lista.append(i)
    cont += 1
    suma += i
cont -= 1
print("El mayor numero es: " + str(max(lista)))
print("El menor numero es: " + str(min(lista)))
print("El promedio es: " + str((suma // cont)))
