v_inicial = float(input("Ingrese velocidad inicial: "))
aceleracion = float(input("Ingrese aceleracion: "))
distancia = float(input("Ingrese distancia: "))
v_final = ((v_inicial**2)+2*aceleracion*distancia)**(0.5)
print("Velocidad final:",v_final,"m/s")