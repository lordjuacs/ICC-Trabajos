lista1 = []
lista2 = []
while True:
    n = int(input())
    if n % 2 == 0:
        if n == 0:
            break
        lista1.append(n)
    else:
        lista2.append(n)

print("Lista de pares:",lista1)
print("Lita de impares:",lista2)
