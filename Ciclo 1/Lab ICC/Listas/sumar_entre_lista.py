lista = [2,3,4,10,5,6]
n = len(lista)
for i in range(n//2):
    print(lista[i] + lista[n-i-1])
