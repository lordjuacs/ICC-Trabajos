cat = str(input("Ingrese categoria: "))
mes = int(input("Ingrese cantidad de veces por mes: "))
tarifa = 0
lista = ["I","II","III","IV","V"]
if cat not in lista:
    print("error")
else:
    if cat == "I":
        tarifa = 5
    elif cat == "II":
        tarifa = 10
    elif cat == "III":
        tarifa = 15
    elif cat == "IV":
        tarifa = 20
    else:
        tarifa = 25
    print("El costo anual es:",tarifa * mes * 12)
