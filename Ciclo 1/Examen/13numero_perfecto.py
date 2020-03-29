def es_perfecto(num):
    divisores = []
    for i in range(1,num):
        if num % i == 0 and i != num:
            divisores.append(i)
    if sum(divisores) == num:
        return True
    else:
        return False
def es_primo(num):
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
    if num > 1:
        return primo
    else:
        return False

min = int(input("Ingrese min: "))
max = int(input("Ingrese max: "))
impresion = []
for i in range(min, max):
    perfecto = es_perfecto(i)
    primo = es_primo(i)
    if (perfecto or primo) and i not in impresion:
        impresion.append(str(i))
if len(impresion) > 0:
    print(" ".join(impresion))
else:
    print("No hay numeros perfectos ni primos")
