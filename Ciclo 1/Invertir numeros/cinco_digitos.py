number_1 = int(input(("Ingrese numero de cinco digitos: ")))
a = (number_1 % 10) * 10000
b = (number_1 // 10)
c = (b % 10) * 1000
d = (b // 10)
e = (d % 10) * 100
f = (d // 10)
g = (f % 10) * 10
h = (f // 10)
number_2 = (a + c + e + g + h)
print(number_2)