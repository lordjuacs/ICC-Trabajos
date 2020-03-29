lista_original = input("Ingresar lista: ").split(",")
for i in range(len(lista_original)):
    lista_original[i] = int(lista_original[i])
indice_maximo = lista_original.index(max(lista_original))
nueva_lista = lista_original.copy()
nueva_lista.pop(indice_maximo)
nueva_lista.insert(0,max(lista_original))
print("Nueva lista:",nueva_lista)