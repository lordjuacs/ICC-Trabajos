cant = int(input())
original = []
nueva = []
suma = 0
for i in range(cant):
    nombre = input()
    original.append(nombre)
for x in range(len(original)-1):
    if original[x] not in nueva:
        nueva.append(original[x])
for _ in nueva:
    print(_)
