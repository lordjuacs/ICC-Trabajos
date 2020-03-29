n = int(input("Ingrese N: "))
max = 29
min = 66
imprime = False
for i in range(1,n+1):
    edad = int(input("Ingrese edad " + str(i) + ": "))
    if edad >= 30 and edad <=65:
        imprime = True
        if edad > max:
            max = edad
        if edad < min:
            min = edad
print(imprime * ("El mayor es: " + str(max)))
print(imprime * ("El menor es: " + str(min)))
