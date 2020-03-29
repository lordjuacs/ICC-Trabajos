import math
def r_menos2a(r,a):
    return (1/r) - (1/(2*a))

gravedad = 6.674 * (10 ** -11)

masa = float(input())
r = float(input())
a = float(input())
v_orbital = math.sqrt(2 * gravedad * masa * r_menos2a(r,a))
print("La velocidad en (m/s) es:",v_orbital)
