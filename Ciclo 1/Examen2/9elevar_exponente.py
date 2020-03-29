def potencia(base, exponente):
    if exponente == 1:
        return base
    else:
        return base * potencia(base, exponente - 1)
base = int(input("Ingrese un numero: "))
expo = int(input("Ingrese el exponente: "))
resultado = potencia(base, expo)
print("El resultado es:", resultado)