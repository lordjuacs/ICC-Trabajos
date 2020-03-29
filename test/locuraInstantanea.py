import Cubo as cb

def listaOpuestos(lCubos):
    op1 = lCubos[0].Opuestos.copy()
    op2 = lCubos[1].Opuestos.copy()
    op3 = lCubos[2].Opuestos.copy()
    op4 = lCubos[3].Opuestos.copy()

    return [op1, op2, op3, op4]

def locuraInstantanea(lOpuestos, size):

    grafo = [("", ""), ("", ""), ("", ""), ("", "")]
    contA = 0
    contB = 0
    contR = 0
    contV = 0

    for i in range(size):
        grafo[0] = lOpuestos[0][i]
        for j in range(size):
            grafo[1] = lOpuestos[1][j]
            for k in range(size):
                grafo[2] = lOpuestos[2][k]
                for l in range(size):
                    grafo[3] = lOpuestos[3][l]
                    for tupla in grafo:
                        for lado in tupla:
                            if lado == "blue":
                                contA += 1
                            elif lado == "white":
                                contB += 1
                            elif lado == "red":
                                contR += 1
                            else:
                                contV += 1
                    if contA == 2 and contB == 2 and contR == 2 and contV == 2:
                        if size == 2:
                            return grafo
                        c1 = lOpuestos[0].copy()
                        c2 = lOpuestos[1].copy()
                        c3 = lOpuestos[2].copy()
                        c4 = lOpuestos[3].copy()
                        c1.pop(i)
                        c2.pop(j)
                        c3.pop(k)
                        c4.pop(l)
                        lC = [c1, c2, c3, c4]
                        grafo2 = locuraInstantanea(lC, 2)
                        if grafo2 != "None":
                            return [grafo, grafo2]
                        else:
                            contA = 0
                            contB = 0
                            contR = 0
                            contV = 0
                    else:
                        contA = 0
                        contB = 0
                        contR = 0
                        contV = 0
    return "None"


def armarTorres(grafo):

    lado1 = []
    lado2 = []
    for opuesto in grafo:
        if opuesto[0] not in lado1 and opuesto[1] not in lado2:
            lado1.append(opuesto[0])
            lado2.append(opuesto[1])
        else:
            lado1.append(opuesto[1])
            lado2.append(opuesto[0])
    return [lado1, lado2]


def Solucion(lCubos):
    lGrafos = locuraInstantanea(listaOpuestos(lCubos), 3)
    if lGrafos == "None":
        return "No hay solución"

    setLados1 = armarTorres(lGrafos[0])
    setLados2 = armarTorres(lGrafos[1])

    lado1 = cb.ladoTorre(setLados1[0], 1)
    lado2 = cb.ladoTorre(setLados1[1], 3)
    lado3 = cb.ladoTorre(setLados2[0], 2)
    lado4 = cb.ladoTorre(setLados2[1], 4)

    return [lGrafos[0], lGrafos[1]]