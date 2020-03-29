palabra = input("Ingrese: ")
for i in range(len(palabra)//2):
    palindromo = False
    if palabra[i] == palabra[len(palabra)-1-i]:
        palindromo = True
print(palindromo)