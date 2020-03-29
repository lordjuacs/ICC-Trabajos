def costos_fijos():
    alquiler = 160
    publicidad = 50
    return alquiler + publicidad

def costos_variables(x):
    if x >= 1 and x < 11:
        c_alumno = 10.00 * 16
        return c_alumno
    elif x >= 11 and x < 16:
        c_alumno = 13.00 * 16
        return c_alumno
    elif x >= 16 and x < 21:
        c_alumno = 17.00 * 16
        return c_alumno
    else:
        c_alumno = 20.00 * 16
        return c_alumno
def evaluorenta(x):
    ingresos = 80 * x
    costos = costos_fijos() + costos_variables(x)
    utilidad = ingresos - costos
    if utilidad > 0:
        return "es rentable"
    else:
        return "no es rentable"

estudiantes = int(input("Ingrese cantidad de estudiantes: "))
print("Resultado: " + evaluorenta(estudiantes))
