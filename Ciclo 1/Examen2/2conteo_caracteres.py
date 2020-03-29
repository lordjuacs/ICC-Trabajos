def contar_caracteres(string):
    dict = {"Espacios": 0, "Letras": 0, "Numeros": 0}
    letras = 0
    numeros = 0
    espacios = 0
    for i in string:
        if i.isalpha():
            letras += 1
        elif i.isdigit():
            numeros += 1
        elif i == " ":
            espacios += 1
    dict["Espacios"] = espacios
    dict["Letras"] = letras
    dict["Numeros"] = numeros
    return dict

def contar_caracteres2(string):
    dic = {"Espacios": 0, "Letras": 0, "Numeros": 0}
    for i in string:
        if i == " ":
            dic["Espacios"] += 1
        elif i.isalpha():
            dic["Letras"] += 1
        elif i.isdigit():
            dic["Numeros"] += 1
    return dic

texto = input("Ingrese un texto: ")
resultado = contar_caracteres(texto)
resultado2 = contar_caracteres2(texto)
print("El diccionario resultado es:", resultado)
print("El diccionario resultado es:", resultado2)