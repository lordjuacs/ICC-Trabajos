numero = input("Ingrese un numero: ")
while int(numero) % 3 != 0:
        numero = input("Ingrese un numero: ")

import time
start = time.time()
while True:
    lista = []
    for i in numero:
        lista.append(int(i) ** 3)
        total = sum(lista)
    print("la suma de cubos de " + numero + " es:",total)
    if total == 153:
        print("la suma de cubos de " + str(total) + " es:", total)
        end = time.time()
        tiempo = end - start
        print("Tiempo demorado:",tiempo)
        break
    numero = str(total)
    total = 0