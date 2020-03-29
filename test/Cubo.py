import turtle


class Lado:
    def __init__(self, color, posX, posY):

        if color == "B":
            self.color = "white"
        elif color == "V":
            self.color = "green"
        elif color == "A":
            self.color = "blue"
        else:
            self.color = "red"

        self.lado = turtle.Turtle()
        self.lado.penup()
        self.lado.shape("square")
        self.lado.color(self.color)
        self.lado.setposition(posX, posY)


class Cubo:
    def __init__(self, lados, nCubo):

        self.lado1 = Lado(lados[0], -200+80*nCubo, 200)
        self.lado2 = Lado(lados[1], -200+80*nCubo, 180)
        self.lado3 = Lado(lados[2], -200+80*nCubo, 160)
        self.lado4 = Lado(lados[3], -200+80*nCubo, 140)
        self.lado5 = Lado(lados[4], -220+80*nCubo, 180)
        self.lado6 = Lado(lados[5], -180+80*nCubo, 180)

        self.Opuestos = [(self.lado1.color, self.lado3.color), (self.lado2.color, self.lado4.color),
                         (self.lado5.color, self.lado6.color)]


class Piso:
    def __init__(self, color, posX, posY):
        self.piso = turtle.Turtle()
        self.piso.penup()
        self.piso.shape("square")
        self.piso.color(color)
        self.piso.setposition(posX, posY)


class ladoTorre:
    def __init__(self, pisos, nTorre):
        self.piso1 = Piso(pisos[0], -200+80*nTorre, 0)
        self.piso2 = Piso(pisos[1], -200+80*nTorre, -20)
        self.piso3 = Piso(pisos[2], -200+80*nTorre, -40)
        self.piso4 = Piso(pisos[3], -200+80*nTorre, -60)