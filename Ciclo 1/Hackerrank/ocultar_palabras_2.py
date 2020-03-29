frase_como_lista = input().split()
cant_palabra_grande = len(max(frase_como_lista, key=len))
count = 0
u = ""
while count != len(frase_como_lista):
    frase_como_lista[count] = frase_como_lista[count] + "@" * (cant_palabra_grande - len(frase_como_lista[count]))
    count += 1
for subindice in range(cant_palabra_grande):
    for element in frase_como_lista:
        u += str(list(element)[subindice])
    print(u, end=" ")
    u = ""