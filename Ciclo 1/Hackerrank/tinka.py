cant = int(input())
lista = []
def revisar_primo(n):
    primo = True
    for x in range(2,n):
        if n % x ==0:
            primo = False
    return primo

for i in range(cant):
    numero = int(input())
    lista.append(numero)
for valor in lista:
    primo = revisar_primo(valor) * 1
    if primo == 1:
        print(valor)