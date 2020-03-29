n = int(input())
resul = 1
for i in range(1, n + 1):
    resul = resul * (4 ** i)
    print("si", resul)
ecuacion = 2 ** (n * (n + 1))
if resul == ecuacion:
    print("si")