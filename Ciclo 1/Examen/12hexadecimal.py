def getHexadecimal(decimal):
    lista = []
    opera = 0
    while True:
        cociente = decimal // 16
        residuo = decimal % 16
        lista.insert(0, residuo)
        decimal = cociente
        opera += 1
        if cociente < 16:
            lista.insert(0, cociente)
            break
    de_verdad = ""
    for i in range(len(lista)):
        if lista[i] == 10:
            de_verdad += "A"
        elif lista[i] == 11:
            de_verdad += "B"
        elif lista[i] == 12:
            de_verdad += "C"
        elif lista[i] == 13:
            de_verdad += "D"
        elif lista[i] == 14:
            de_verdad += "E"
        elif lista[i] == 15:
            de_verdad += "F"
        else:
            de_verdad += str(lista[i])
    return de_verdad

decimal = int(input("Ingrese un numero decimal: "))
impresion = getHexadecimal(decimal)
print("El equivalente en Hexadecimal es:",impresion)