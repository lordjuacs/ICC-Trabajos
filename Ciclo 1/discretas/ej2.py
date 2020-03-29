n = int(input())
bandera = False

for i in range(1, n + 1):
    ecuacion = 3 ** (2 * n + 4) - 2 ** (n - 1)
    if ecuacion % 7 == 0:
        bandera = True
        print("si", i)
    else:
        bandera = False
        print("no", i)
        break
