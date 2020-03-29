n = int(input())
lista = []
for i in range(n):
    palabra = input()
    if len(palabra) > 4:
        lista.append(palabra)
print(",".join(lista))