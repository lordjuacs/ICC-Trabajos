number_1 = int(input(("Ingrese numero de tres digitos: ")))
a = (number_1 % 10) * 100
b = (number_1 // 10)
c = (b % 10) * 10
d = (b // 10)
number_2 = (a + c + d)
print(number_2)