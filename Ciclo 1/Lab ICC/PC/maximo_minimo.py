n = int(input("Ingrese el primer numero: "))
m = int(input("Ingrese el segundo numero: "))
d = min(n,m)
while m % d != 0 or n % d != 0:
        d -= 1
print("MCD:",d)
