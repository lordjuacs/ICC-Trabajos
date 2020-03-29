def conteo(entrada):
    lista = []
    for i in entrada:
        u = ""
        for letra in i:
            if letra.isdigit() or letra == ".":
                u += letra
        lista.append(u)
    for i in lista:
        if i == "":
            lista.remove(i)
    unicos = []
    for i in lista:
        if i not in unicos:
            unicos.append(i)
    for i in unicos:
        veces = lista.count(i)
        print(i, "=", veces)
entrada = input("Ingrese la lista de numeros decimales: ").split(" ")
conteo(entrada)

