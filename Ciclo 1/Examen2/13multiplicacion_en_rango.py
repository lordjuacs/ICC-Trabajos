def multiplicacion(inicio, tope):
    if inicio == tope:
        return tope
    else:
        return inicio * multiplicacion(inicio + 1, tope)
n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese un número: "))
resultado = multiplicacion(min(n1, n2), max(n1, n2))
print("Resultado:", resultado)