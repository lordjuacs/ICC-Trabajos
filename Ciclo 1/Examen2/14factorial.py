def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese numero: "))
resultado = factorial(numero)
print("Resultado:", resultado)