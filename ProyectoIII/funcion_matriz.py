# se importa ast para poder leer el archivo .txt del diccionario general y convertirlo de string a diccionario
import ast
from funcion_quicksort import *


def matriz_de_datos():
    filepath = "jugadores_puntaje.txt"

    manejando = open(filepath, "r")
    datos = manejando.read()
    diccionario_en_uso = ast.literal_eval(datos)

    lista_personas = list(diccionario_en_uso.keys())
    lista_pre_scores = list(diccionario_en_uso.values())
    lista_scores = [int(i) for i in lista_pre_scores]

    matrix = []
    for i in range(len(lista_personas)):
        fila_de_datos = []
        fila_de_datos.append(lista_scores[i])
        fila_de_datos.append(lista_personas[i])
        matrix.append(fila_de_datos)
    quickSort(matrix, 0, len(matrix) - 1)

    return matrix
