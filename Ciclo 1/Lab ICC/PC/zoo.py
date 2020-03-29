precio_total=0
cant=int(input("ingrese la cantidad de visitantes:"))
for i in range(1,cant+1):
  edad = int(input("ingrese la edad del visitante #" + str(i) + ": "))
  if edad >= 0 and edad <= 100:
    if edad > 2 and edad < 13:
      precio_total = precio_total + 14
    elif edad >= 13 and edad < 65:
      precio_total = precio_total + 23
    elif edad >= 65:
      precio_total = precio_total + 18
    else:
      precio_total = precio_total + 0
  else:
      print("la edad del visitante # " + str(i) + " es incorrecta, ingrese nuevamente")
      x = i
      while True:
          edad = int(input("ingrese la edad del visitante #" + str(x) + ": "))
          if edad >= 0 and edad <= 100:
              if edad > 2 and edad < 13:
                  precio_total = precio_total + 14
              elif edad >= 13 and edad < 65:
                  precio_total = precio_total + 23
              elif edad >= 65:
                  precio_total = precio_total + 18
              else:
                  precio_total = precio_total + 0
              break
print("el precio total es:", precio_total)