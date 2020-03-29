cant = int(input())
desaprobados = []
notas = []
suma = 0
for i in range(cant):
    (name,grade) = input().split(",")
    grade = float(grade)
    if grade < float(10.5):
        desaprobados.append(name)
        notas.append(float(grade))
    else:
        suma += grade
minima = suma / (cant - len(desaprobados))
for valor in range(len(desaprobados)):
    necesario = minima - float(notas[valor])
    print(desaprobados[valor]+","+str(necesario))