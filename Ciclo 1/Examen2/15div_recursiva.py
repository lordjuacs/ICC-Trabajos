def division(dividendo, divisor):
    if dividendo == 0:
        return 0
    else:
        return 1 + division(dividendo - divisor, divisor)

dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))
resultado = division(dividendo, divisor)
print("Resultado: ", resultado)