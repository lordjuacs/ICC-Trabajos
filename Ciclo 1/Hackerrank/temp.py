def suma(lista, tamano):
  bandera = False
  for valor in lista:
    for i in range(tamano):
        a = lista[i]
        b = lista[i - 1 + 1]
        if valor == a + b:
            bandera = True
  return bandera

tamano = int(input())
numeros = input().split(" ")
for i in range(tamano):
  numeros[i] = int(numeros[i])
efe = suma(numeros, tamano)
if efe == True:
  print("yes")
else:
  print("no")