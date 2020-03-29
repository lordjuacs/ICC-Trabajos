ingresa = input("Ingrese un numero o texto: ")

for i in range(len(ingresa)//2):
    no_es = True
    if ingresa[i] == ingresa[len(ingresa)-1-i]:
        no_es = False

if ingresa[0] in ["0","1","2","3","4","5","6","7","8","9"]:
    impresion = ingresa + " no" * no_es + " es un numero capicua."
    print(impresion)
else:
    impresion = ingresa + " no" * no_es + " es un texto palindromo."
    print(impresion)
