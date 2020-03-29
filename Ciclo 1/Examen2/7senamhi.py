def menor(d):
    menor = 100
    fecha = ""
    for e in d:
        if d[e] < menor:
            menor = d[e]
            fecha = e
    return fecha


def mayor(d):
    mayor = 0
    fecha = ""
    for e in d:
        if d[e] > mayor:
            mayor = d[e]
            fecha = e
    return fecha


lima = {"22/05/2019": 17, "23/05/2019": 17, "24/05/2019": 19, "25/05/2019": 23, "26/05/2019": 20, "27/05/2019": 18,
        "28/05/2019": 20, "29/05/2019": 19, "30/05/2019": 22, "31/05/2019": 19, "01/06/2019": 20, "02/06/2019": 19,
        "03/06/2019": 17, "04/06/2019": 16, "05/06/2019": 18, "06/06/2019": 21, "07/06/2019": 19, "08/06/2019": 15,
        "09/06/2019": 17, "10/06/2019": 20, "11/06/2019": 15, "12/06/2019": 22, "13/06/2019": 14, "14/06/2019": 16}

datos_extra = int(input("Ingrese la cantidad de datos a agregar: "))
for i in range(datos_extra):
    fecha = input("Ingrese la fecha: ")
    temperatura = int(input("Ingrese la temperatura: "))
    lima[fecha] = temperatura
temp_mayor = mayor(lima)
temp_menor = menor(lima)
print("La fecha mas baja es:", temp_menor)
print("La fecha mas alta es:", temp_mayor)
