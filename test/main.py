import turtle
import time
import Cubo as cb
import locuraInstantanea as loc

cubo1 = cb.Cubo(input().split(), 1)
cubo2 = cb.Cubo(input().split(), 2)
cubo3 = cb.Cubo(input().split(), 3)
cubo4 = cb.Cubo(input().split(), 4)


print("Opuestos 1:", end=" ")
print(cubo1.Opuestos)
print("Opuestos 2:", end=" ")
print(cubo2.Opuestos)
print("Opuestos 3:", end=" ")
print(cubo3.Opuestos)
print("Opuestos 4:", end=" ")
print(cubo4.Opuestos)


lCubos = [cubo1, cubo2, cubo3, cubo4]

print()
print(loc.Solucion(lCubos))


# ----- Screen Setup
screen = turtle.Screen()
screen.bgcolor("gray")
screen.title("Cubos")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off screen updates

# ----- Screen Update
delay = 0.1
while True:
    screen.update()
    time.sleep(delay)