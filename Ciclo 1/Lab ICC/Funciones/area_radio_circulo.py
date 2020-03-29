import math
def calcArea(radio):
    return (radio ** 2) * math.pi


radio = float(input("Radio: "))
area = calcArea(radio)
print("El area es:",area)
