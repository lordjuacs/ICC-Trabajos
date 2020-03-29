n = int(input("Filas: "))
for x in range(n):
    #imprimir espacios en blanco
    for y in range(n-x-1):
        print("",end=" ")
    #imprimir asteriscos
    for y in range(x+1):
        print("*",end="")
    print()


n = int(input("Filas: "))
for x in range(n):
    #imprimir espacios en blanco
    print(" "*(n-x-1),end="")
    #imprimir asteriscos
    print("*"*(x+1),end="")
    print()

