numero = int(input())
numero_lista = []

if len(str(numero)) <= 15:

    for x in str(numero):
        numero_lista.append(int(x))
    length = len(str(numero))
    tank = len(numero_lista) // 2
    print(tank)
    for i in range(0, length//2):
        suma = 0
        length -= 1
        suma = numero_lista[i] + numero_lista[length]
        print(suma)
    if len(str(numero)) % 2 != 0:
        plane = numero_lista[len(str(numero)) // 2]
        print(plane)
    else:
        plane = 0
        print(plane)
