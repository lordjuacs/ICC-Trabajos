palabra = input("input: ")
lista = []
for i in range(1,len(palabra)):
    if i == 1:
        lista.append(palabra[i].upper())
    else:
        lista.append(palabra[i])
lista.append(palabra[0].lower())
lista.append("bot")
print("".join(lista))