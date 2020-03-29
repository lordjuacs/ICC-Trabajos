from math import *
#hay 10 funciones

def dxⁿ(valor_de_x, exp):
    coeficiente = exp
    nuevo_exp = exp - 1
    resultado = coeficiente * (valor_de_x ** nuevo_exp)
    return resultado


def daˣ(valor_de_x, valor_de_a):
    coeficiente = valor_de_a ** valor_de_x
    ln = log(valor_de_a)
    resultado = coeficiente * ln
    return resultado


def dlnx(valor_de_x):
    resultado = 1 / valor_de_x
    return resultado


def deˣ(valor_de_x):
    resultado = e ** valor_de_x
    return resultado


def dsinx(valor_de_x):
    resultado = cos(valor_de_x)
    return resultado


def dcosx(valor_de_x):
    resultado = -1 * (sin(valor_de_x))
    return resultado


def dtgx(valor_de_x):
    resultado = 1/(cos(valor_de_x)**2)
    return resultado


def dctgx(valor_de_x):
    resultado = -1 * (1/(sin(valor_de_x)**2))
    return resultado


def dsecx(valor_de_x):
    resultado = (1 / cos(valor_de_x)) * (tan(valor_de_x))
    return resultado


def dcscx(valor_de_x):
    resultado = -1 * (1/tan(valor_de_x)) * (1/sin(valor_de_x))
    return resultado

