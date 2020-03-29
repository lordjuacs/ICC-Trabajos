def repeticion(string):
    caracter = [" "]
    mas_repetido = 0
    for i in string:
        if string.count(i) > mas_repetido and i != " ":
            mas_repetido = string.count(i)
            caracter.pop(0)
            caracter.insert(0,i)
    return "".join(caracter)
frase1 = input("Ingrese la frase 1: ")
frase2 = input("Ingrese la frase 2: ")
frase3 = input("Ingrese la frase 3: ")
de1 = repeticion(frase1)
de2 = repeticion(frase2)
de3 = repeticion(frase3)
impresion = de1 + de2 + de3
print(impresion)