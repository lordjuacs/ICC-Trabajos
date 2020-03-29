import time
n = int(input())
suma = 0
start_for = time.time()
for i in range(1, n + 1):
    suma += ((3*i - 2)*(3 * i + 1))**-1
end_for = time.time()
diferencia_for = end_for - start_for
print("suma con ecuacion: ", suma)
print("tiempo del for:", diferencia_for)
start_ecu = time.time()
efe = n / (3 *n +1)
end_ecu = time.time()
diferencia_ecu = end_ecu - start_ecu
print("suma n al cuadrado:", efe)
print("tiempo de la ecu:", diferencia_ecu)
