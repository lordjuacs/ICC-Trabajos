def construccion_dic(n):
    dic = {}
    for i in range(1, n + 1):
        (fecha, valor) = input("Registro " + str(i) + ": ").split(" ")
        if fecha in list(dic.keys()):
            dic[fecha].append(float(valor))
        else:
            dic[fecha] = []
            dic[fecha].append(float(valor))
    return dic

def mayor(d):
    maximo = 0
    for e in d:
        evaluar = max(d[e])
        if evaluar > maximo:
            maximo = evaluar
            dia = e
    return dia

n = int(input("ingrese cantidad de datos: "))
diccionario = construccion_dic(n)
diaxd = mayor(diccionario)
print("el diccionario es:", diccionario)
print("el dia con mayor es: " + diaxd)