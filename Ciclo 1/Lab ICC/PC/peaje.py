categoria = str(input("Ingrese la categoria del vehiculo: "))
cant_mes = int(input("Ingrese la cantidad de veces por mes: "))
if categoria == "I":
    costo1 = int(5*cant_mes*12)
    print("Cosoto anual" + str(costo1))
elif categoria == "II":
    costo2 = int(10*cant_mes*12)
    print("Cosoto anual" + str(costo2))
elif categoria == "III":
    costo3 = int(15*cant_mes*12)
    print("Cosoto anual" + str(costo3))
elif categoria == "IV":
    costo4 = int(20*cant_mes*12)
    print("Cosoto anual" + str(costo4))
else:
    costo5 = int(25*cant_mes*12)
    print("Costo anual: " + str(costo5))
