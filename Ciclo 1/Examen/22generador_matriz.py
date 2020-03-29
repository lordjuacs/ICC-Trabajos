def generar_matriz(filas, columnas, elemento = "a"):
    for i in range(filas):
        for j in range(columnas):
            print(elemento, end=" ")
        print()


FILAS = int(input("Ingrese el numero de filas: "))
COLUMNAS = int(input("Ingrese el numero de Columnas: "))
print("La matriz con " + str(FILAS) + " filas y " + str(COLUMNAS) + " columnas es la siguiente:")
generar_matriz(FILAS, COLUMNAS)
