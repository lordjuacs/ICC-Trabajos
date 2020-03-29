def extrae_intervalo(lista, inf=0, sup=100):
    impresion = []
    for i in lista:
        if i >= inf and i <= sup:
            impresion.append(str(i))
    return " ".join(impresion)
ingrese_lista = []
temp = input("Ingrese los numeros de su lista: ").split(" ")
for i in temp:
    ingrese_lista.append(int(i))
inferior = int(input("Ingrese el limite inferior: "))
superior = int(input("Ingrese el limite superior: "))
print(extrae_intervalo(ingrese_lista, inferior, superior))
print(extrae_intervalo(ingrese_lista))