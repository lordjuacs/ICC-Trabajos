max = 0
min = 1000
suma = 0
for i in range(0,7):
    n = int(input())
    suma = suma + n
    if n > max:
        max = n
    if n < min:
        min = n
print(max)
print(min)
print(suma // 7)