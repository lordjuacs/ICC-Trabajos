def naturales(tope, cont = 1):
    if cont == tope:
        return str(tope)
    else:
        return str(cont) + " " + naturales(tope, cont + 1)

numero = int(input("Ingrese un numero: "))
resultado = naturales(numero)
print("Los números son:", resultado)


def owo(x):
    if x == 1:
        return 1
    else:
        return str(owo(x - 1)) + " " + str(x)

x = int(input())
print("result:", owo(x))
