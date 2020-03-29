print("input")
primera = input()
segunda = input()
tercera = []
primera_lista = []

for i in primera:
    primera_lista.append(i)

for i in segunda:
    if i not in primera:
        tercera.append(i)
print("".join(tercera))