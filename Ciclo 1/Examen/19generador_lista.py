from random import randint
tamano = int(input("Ingrese la cantidad: "))
lista1 = []
lista2 = []
for i in range(tamano):
    lista1.append(randint(1, tamano // 3))
for i in lista1:
    if lista1.count(i) >= 3 and i not in lista2:
            lista2.append(i)
print("Lista original:", lista1)
print("Lista solicitada:", lista2)