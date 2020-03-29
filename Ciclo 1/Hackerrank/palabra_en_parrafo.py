parrafo = str(input())
palabra = str(input())
encontro = parrafo.count(palabra)
print(encontro)

parrafo = str(input())
palabra = str(input())
length = int(len(palabra))
count = 0
union = ""
for i in range(len(parrafo)):
    if parrafo[i:i + length] == palabra:
        count += 1
print(count)
