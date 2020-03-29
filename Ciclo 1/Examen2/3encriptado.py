def hacer_diccionario():
    dic = {}
    cont = 0
    for i in range(ord('a'), ord('n') + 1):
        cont += 1
        dic[chr(i)] = cont
    cont += 1
    dic['ñ'] = cont
    for i in range(ord('o'), ord('z') + 1):
        cont += 1
        dic[chr(i)] = cont
    return dic

def traducir(string, diccionario):
    u = ""
    for i in string:
        n = str(diccionario[i])
        u += n
    return u

texto = input("Ingrese un texto: ").lower()
dic = hacer_diccionario()
print(dic)
efe = traducir(texto, dic)
print("El mensaje encriptado es:", int(efe))
