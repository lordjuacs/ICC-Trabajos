alumnos = int(input())
lista = []
suma = 0
for i in range(alumnos):
    (sex,age) = input().split(",")
    lista.append(sex)
    suma += int(age)
hombres = lista.count("H")
mujeres =lista.count("M")
porce_h = hombres / alumnos
porce_m = mujeres / alumnos
promedio = round(suma /alumnos)
print(porce_h)
print(porce_m)
print(promedio)