def imprimeserie(numero, decremento):
    if numero in range(-3, 4):
        return numero
    else:
        return imprimeserie(numero - decremento, decremento)
n = int(input("Ingrese numero: "))
decre = int(input("Ingrese decremento: "))
resultado = imprimeserie(n, decre)
print("Resultado:", resultado)