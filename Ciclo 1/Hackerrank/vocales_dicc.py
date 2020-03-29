def contarVocales(texto):
    dic = {'a': 0,'e': 0,'i': 0,'o': 0,'u': 0}
    for i in texto:
        if i.lower() in ["a", "e", "i", "o", "u"]:
            dic[i.lower()] += 1
    return dic


def buscarMayor(dic):
    mayor = 0
    vocal = ""
    for e in dic:
        if dic[e] > mayor:
            mayor = dic[e]
            vocal = e
    return (vocal, dic[vocal])
# Escriba el cuerpo de la funcion que busca la mayor ocurrencia

texto = input("")
dicVocales = contarVocales(texto)
if sum(dicVocales.values()) == 0:
    print("ERROR")
else:
    print(buscarMayor(dicVocales))