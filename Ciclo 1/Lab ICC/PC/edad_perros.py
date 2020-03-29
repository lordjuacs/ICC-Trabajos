anos_h=int(input("ingrese años humanos: "))

if anos_h >= 0 and anos_h <= 2:
  print ("la edad del perro es:", int(anos_h*10.5) )
elif anos_h >2 and anos_h <=30:
  xtra= anos_h - 2
  print ("la edad del perro es:", int(21+4*xtra))
else:
  print("los años humanos es incorrecto (menor de 0 y mayor")