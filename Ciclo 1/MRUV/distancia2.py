v_inicial = float(input("Ingrese velocidad inicial: "))
tiempo = float(input("Ingrese tiempo: "))
aceleracion = float(input("Ingrese aceleracion: "))
distancia = (v_inicial*tiempo)+((aceleracion*tiempo**2))/2
print("Distancia:",distancia,"m")