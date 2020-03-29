from random import randint
tamano = int(input("Ingrese la cantidad: "))
lista1 = []
lista2 = []
for i in range(tamano):
    lista1.append(randint(1, tamano // 3))
for i in range(len(lista1)-1):
    if lista1[i]+ 1 == lista1[i+1]:
        lista2.append(lista1[i])
print("Lista original:", lista1)
print("Lista solicitada:", lista2)