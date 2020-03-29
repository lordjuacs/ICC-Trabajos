def armonico(numero, cont=1):
    if cont == numero:
        return numero ** -1
    else:
        return armonico(numero, cont + 1) + cont ** -1


entrada = int(input("Input: "))
resultado = round(armonico(entrada), 3)
print("Output", resultado)