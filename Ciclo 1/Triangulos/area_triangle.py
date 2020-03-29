lado_1 = float(input("Ingrese medida lado 1: "))
lado_2 = float(input("Ingrese medida lado 2: "))
lado_3 = float(input("Ingrese medida lado 3: "))
si_triangulo = (lado_1 + lado_2 > lado_3) and (lado_1 + lado_3 > lado_2) and (lado_2 + lado_3 > lado_1)
s = (lado_1 + lado_2 + lado_3)/2
area = round((s * (s - lado_1) * (s - lado_2 ) * (s - lado_3))**0.5,2)
respuesta = (not si_triangulo) * "NO ES TRIANGULO" + (si_triangulo) * ("EL AREA ES: " + str(area) + " m^2")
print(respuesta)