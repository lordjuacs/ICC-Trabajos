def insertion_sort_ascendente(lista):
    for i in range(1, len(lista)):
        h = i
        while h > 0 and lista[h] < lista[h - 1]:
            aux = lista[h]
            lista[h] = lista[h - 1]
            lista[h - 1] = aux
            h -= 1


def ordenar_ventas(dic):
    lista = list(dic.values())
    insertion_sort_ascendente(lista)
    return lista

ventas = {"Xiaomi": 96, "Oppo": 119, "LG": 55.9, "Lenovo": 49.9,
          "Nokia": 7.7, "TecnoPro": 13.1, "Dell": 6.1, "IBM": 0.6,
          "Sahito": 34.6, "Samsung": 318.1, "Apple": 215.8, "Vivo": 100.2,
          "Huawei": 153.1, "Aio": 45.6, "FirePhone": 29.7, "Motorola": 20.3}

ordenada = ordenar_ventas(ventas)
baja = ordenada[0]
alta = ordenada[len(ordenada) - 1]

print("Ventas ordenadas:", ordenada)
print("Venta mas baja:", baja)
print("Venta mas alta:", alta)
