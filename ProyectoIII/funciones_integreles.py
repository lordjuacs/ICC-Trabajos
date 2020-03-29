from math import *
#hay 10 funciones

def ixⁿ(valor_exponte, low, high):
    nuevo_exponente = valor_exponte + 1
    coeficiente = nuevo_exponente
    up = (high ** nuevo_exponente) / coeficiente
    down = (low ** nuevo_exponente) / coeficiente
    resultado = up - down
    return resultado


def iaˣ(valor_a, low, high):
    up = (valor_a ** high) / log(valor_a)
    down = (valor_a ** low) / log(valor_a)
    resultado = up - down
    return resultado


def ieˣ(low,high):
    low= e**low
    high= e**high
    resultado = high-low
    return resultado


def i1entrex(low, high):
    up = log(high)
    down = log(low)
    resultado = up - down
    return resultado


def isinx(low, high):
    up = -1 * cos(high)
    down = -1 * cos(low)
    resultado = up - down
    return resultado


def icosx(low, high):
    low = sin(low)
    high = sin(high)
    resultado = high-low
    return resultado


def itgx(low, high):
    up = log(abs(1/cos(high)))
    down = log(abs(1/cos(low)))
    resultado = up - down
    return resultado


def ictg(low, high):
    low = log(abs(sin(low)))
    high = log(abs(sin(high)))
    resultado = high - low
    return resultado


def i_1entresqrt1menosxcuadrado(low,high):
    low = asin(low)
    high = asin(high)
    resultado = high-low
    return resultado


def imenos1entresqrt1menosxcuadrado(low, high):
    up = acos(high)
    down = acos(low)
    resultado = up - down
    return resultado

