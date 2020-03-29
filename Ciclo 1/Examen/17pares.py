pares = []
while True:
    numero = int(input())
    if numero == 0:
        break
    if numero % 2 == 0:
        pares.append(numero)
print(pares)