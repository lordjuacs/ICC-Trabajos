input_file = open("empleados.txt", "r")
for cadena in input_file:
    nombres, ocupacion, salario = cadena.split(",")
    nombre, apellido = nombres.split()
    salario = int(salario)
    print("Nombres:", apellido, nombre, end=" ")
    print("Ocupacion:", ocupacion, end=" ")
    print("Salario:", salario)
input_file.close()
