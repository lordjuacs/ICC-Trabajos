import random
alumnos = ["Diego", "Jose", "Paolo", "Maria", "Fernanda"]
calificaciones = []
for i in range(len(alumnos)):
    notas = []
    for j in range(5):
        nota_alumno = random.randint(0, 20)
        notas.append(nota_alumno)
    calificaciones.append(notas)
dic = {}

for i in range(len(alumnos)):
    dic[alumnos[i]] = calificaciones[i]

mejor = 0
peor = 20
for e in dic:
    promedio = sum(dic[e]) / 5
    if promedio > mejor:
        mejor_alumno = e
        mejor = promedio
    if promedio < peor:
        peor_alumno = e
        peor = promedio


print("Mejor alumno:", mejor_alumno, mejor)
print("Peor alumno:", peor_alumno, peor)

for i in dic:
    if sum(dic[i]) / 5 < 10.5:
        del dic[i]
print(dic)
