def obtenerDias(dia,mes, ano):
    enero = 14
    febrero = 28
    marzo = 31
    abril = 30
    mayo = 31
    junio = 30
    julio = 31
    agosto = 31
    setiembre = 30
    octubre = 31
    noviembre = 30
    diciembre = 31
    lista = [enero, febrero, marzo, abril, mayo, junio, julio, agosto, setiembre, octubre, noviembre, diciembre]
    suma = 0
    for i in range(0, int(mes)-1):
        suma += lista[i]
    suma += int(dia)
    if int(ano) >= 2020:
        suma += (365) * (int(ano) - 2019)
    return suma



dia = input("Ingrese dia: ")
mes = input("Ingrese mes: ")
ano = input("Ingrese ano: ")
faltantes = obtenerDias(dia, mes, ano)
print("Dias faltantes:", faltantes)
