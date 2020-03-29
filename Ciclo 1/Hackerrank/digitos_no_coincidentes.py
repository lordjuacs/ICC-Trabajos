def convertir_lista(a):
    prelista = str(a)
    lista = []
    for i in prelista:
        lista.append(int(i))
    return lista
numero1 = int(input())
numero2 = int(input())

lista1 = convertir_lista(numero1)
lista2 = convertir_lista(numero2)

if lista1[0] == lista2[0]:
    lista1[0] = 0
    lista2[0] = 0
if lista1[1] == lista2[1]:
    lista1[1] = 0
    lista2[1] = 0
if lista1[2] == lista2[2]:
    lista1[2] = 0
    lista2[2] = 0
if lista1[3] == lista2[3]:
    lista1[3] = 0
    lista2[3] = 0

new_numero1 = 0
for i in range(len(lista1)):
    new_numero1 += lista1[i] * 10 ** (len(lista1) - i - 1)
new_numero2 = 0
for i in range(len(lista2)):
    new_numero2 += lista2[i] * 10 ** (len(lista2) - i -1)
print("a =",new_numero1)
print("b =",new_numero2)
print("total =",new_numero1 + new_numero2)