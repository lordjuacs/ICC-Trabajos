datos = {}
cont = 1
while True:
    dni = input("Dni " + str(cont) + ": ")
    if len(dni) == 8:
        datos[cont] = dni
        cont += 1
    if dni == "-1":
        break
    if len(dni) != 8:
        print("DNI INCORRECTO")
mayor = 0
elegido = ""
for e in datos:
    if int(datos[e]) > mayor:
        mayor = int(datos[e])

print("El DNI con maximo valor es:", mayor)
print("FIN")