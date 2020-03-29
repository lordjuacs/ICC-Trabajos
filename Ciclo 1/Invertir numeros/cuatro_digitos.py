number_1 = int(input(("Ingrese numero de cuatro digitos: ")))
a = (number_1 % 10) * 1000
b = (number_1 // 10)
c = (b % 10) * 100
d = (b // 10)
e = (d % 10) * 10
f = (d // 10)
number_2 = (a + c + e + f)
print(number_2)