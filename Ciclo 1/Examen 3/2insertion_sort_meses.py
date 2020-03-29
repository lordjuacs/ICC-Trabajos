def insertion_sort_descendente(lista):
    for i in range(1, len(lista)):
        h = i
        while h > 0 and lista[h] > lista[h - 1]:
            aux = lista[h]
            lista[h] = lista[h - 1]
            lista[h - 1] = aux
            h -= 1

meses = []
while True:
    mes = input("Mes: ")
    if mes == "FIN":
        break
    elif mes in ["enero", "febrero", "marzo", "abril", "mayo", "junio",
               "julio", "agosto", "setiembre", "octubre", "noviembre", "diciembre"]:
        meses.append(mes)
    else:
        print("ERROR")

insertion_sort_descendente(meses)
print("Lista ordenada descendente:")
for i in meses:
    print(i)
