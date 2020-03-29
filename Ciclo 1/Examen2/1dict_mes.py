def dar_valor(diccionario, indice):
    return diccionario[indice]

def dar_indice(diccionario, valor):
    return diccionario[valor]

dic1 = {}
dic2 = {}
while True:
    (clave, valor) = input().split(" ")
    if clave == "X":
        break
    dic1[int(clave)] = valor
    dic2[valor] = clave


index = int(input("Ingrese el indice: "))
efe = dar_valor(dic1, index)
print("El mes con el indice igual a " + str(index) + " es:", efe)
value = input("Ingrese el valor: ")
ofo = dar_indice(dic2, value)
print("El indice con valor igual a " + value + " es: " + ofo)
