N = int(input())
nombres = []
edades = []
for i in range(N):
    (name,age) = input().split(",")
    if int(age) > 0:
        nombres.append(name)
        edades.append(int(age))
    sumas = sum(edades)
    promedio = sumas / N
for valor in range(len(edades)):
    if edades[valor] > promedio:
        impresion = str(nombres[valor]) + "," + str(edades[valor])
        print(impresion)