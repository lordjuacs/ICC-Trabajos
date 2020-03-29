import ast
# en esta libreria estan guardadas todas las funciones que trabajan con archivos .txt
from funciones_modo_quiz import *
# en esta libreria esta la funcion para crear la matriz de persona - puntaje
import funcion_matriz
# se importa time para calcular el tiempo que dura el quiz del usuario
import time
# se importa random para utilizar choice(), para poder escoger un elemento aleatorio de una lista
import random
# se importa esta libreria para ejecutar sonidos
from funcion_sounds import *


# esta CLASE será utilizada para poner ciertas palabras en NEGRITA
class Style:
    BOLD = '\033[1m'
    END = '\033[0m'

# la funcion juego() sintetiza a todas las otras funciones, para que en el main vaya solo lo esencial


def jugar():
    filepath = "jugadores_puntaje.txt"

    manejando = open(filepath, "r")
    datos = manejando.read()
    # ast.literal_eval() es una funcion que lee un string y lo convierte en diccionario
    diccionario_en_uso = ast.literal_eval(datos)
    # este diccionario es el que almacena las preguntas(derivadas) como keys,
    # y como values tiene las posibles respuestas
    # de cada uno.
    dic_modo_aventura = {"x²": {"a": "2x", "b": "x/2", "c": "4x"}, "ln(x)": {"a": "log(x)", "b": "1/x", "c": "ex"},
                         "eˣ": {"a": "0", "b": "MathError", "c": "eˣ"}, "4x⁴": {"a": "16", "b": "16x³", "c": "1"},
                         "√x": {"a": "1/2√x", "b": "x¹÷²", "c": "2x"},
                         "cos(x)": {"a": "cos⁻¹(x)", "b": "-1", "c": "-sin(x)"},
                         "tan(x)": {"a": "1/x", "b": "sec²(x)", "c": "sin(x) + cos(x)"},
                         "xᵉ": {"a": "exᵉ-¹", "b": "xᵉ", "c": "eˣ"},
                         "x/ln(x)": {"a": "ln(x)-1/ ln²(x)", "b": "MathError", "c": "ln(x-1)"},
                         "arcsin(x)": {"a": "cos(2x)", "b": "1/√(1-x²)", "c": "sin(x)"}}
    # este diccionario almacena las preguntas (derivadas) como keys, y como values tiene LA RESPUESTA CORRECTA
    dic_aventura_correctas = {"x²": "a", "ln(x)": "b", "eˣ": "c", "4x⁴": "b", "√x": "a", "cos(x)": "c", "tan(x)": "b",
                              "xᵉ": "a", "x/ln(x)": "a", "arcsin(x)": "b"}

    play_sound("fondo.wav")
    intento = 0
    inicio = time.time()
    usuario_score = crear_persona_puntaje(str(intento))
    persona = usuario_score[0]
    dic_temp = update_dict(diccionario_en_uso, usuario_score)
    cambiar_txt_dict("jugadores_puntaje.txt", dic_temp)
    # estas listas corresponden a listas de keys y values de diccionarios. Serán utilizadas al llamar a las preguntas
    # random, entonces cada vez que una es impresa, tiene que ser eliminada, para que no pueda volver a ser llamada
    lista_preguntas = list(dic_modo_aventura.keys())
    lista_opciones = list(dic_modo_aventura.values())
    lista_clave_correcta = list(dic_aventura_correctas.values())

    cont = 1
    play_sound("correct.wav")
    for i in range(len(lista_preguntas)):
        escogido = random.choice(lista_preguntas)
        index = lista_preguntas.index(escogido)
        dic_local = dict(lista_opciones[index])
        print(Style.BOLD + str(cont) + Style.END + ". La derivada de", Style.BOLD + escogido + Style.END, "es:")
        lista_preguntas.remove(escogido)
        lista_opciones.remove(lista_opciones[index])
        for e in dic_local:
            print(Style.BOLD + e + Style.END + ".", dic_local[e])
        while True:
            respuesta = input("Ingresa tu respuesta: ")
            if respuesta == lista_clave_correcta[index]:
                play_sound("correct.wav")
                print("¡Bien hecho!")
                print("¡Ganaste 50 puntos!")
                print()
                cont += 1
                intento += 50
                lista_clave_correcta.pop(index)
                break
            elif respuesta not in ["a", "b", "c"]:
                play_sound("invalid.wav")
                print("Opción inválida, ingrese otra respuesta.")
                print("Perdiste 5 puntos.")
                intento -= 5
                print()
            else:
                play_sound("incorrect.wav")
                print("Te equivocaste, huele a bika.")
                print("Perdiste 25 puntos. ¡Usa nuestra calculadora!")
                print()
                intento -= 25


    final = time.time()
    duracion = final - inicio
    if duracion < 20:
        print("¡Wow, eres una bala! Tienes 15 puntos extra por la rapidez.")
        intento += 15

    elif 20 <= duracion <= 50:
        print("Ganaste 5 puntos por la consistencia de tus respuestas.")
        intento += 5

    else:
        print("Lento, pero seguro.")
        intento += 0
    # aca se actualiza el score del usuario
    usuario_nuevo_score = update_persona_puntaje(persona, str(intento))
    dic_temp2 = update_dict(diccionario_en_uso, usuario_nuevo_score)
    cambiar_txt_dict("jugadores_puntaje.txt", dic_temp2)
    print()
    print(Style.BOLD + "Final del juego" + Style.END)
    print("Tu puntaje fue de: " + Style.BOLD + str(intento) + Style.END)
    print(Style.BOLD + "Suerte en el Hito" + Style.END)
    print()
    print()

    # la matriz con cada persona y su respectivo puntaje
    matriz = funcion_matriz.matriz_de_datos()

    # Imprime encabezado
    print(Style.BOLD + "            Tabla  de  Posiciones" + Style.END)
    print("            Nombre     Puntaje")
    for i in range(len(matriz)):
        # Procesa la i-ésima fila.
        print("%18s" % matriz[i][1], end=" ")
        for j in range(1):
            # Procesa la j-ésima columna en la i-ésima fila
            print("%8d" % (matriz[i][0]))
    print()
    print()
    print("Eso fue todo por hoy, gracias por participar.\nDisfrute de: " + Style.BOLD + "\"Celebration\""
          + Style.END + " by " + Style.BOLD + "Kool & The Gang." + Style.END)
    print()
    print(Style.BOLD + "Integrantes:\n" + Style.END +
                       "✓ Paolo Morey\n"
                       "✓ Joaquín Ramírez\n"
                       "✓ José Porres\n")
    print(Style.BOLD + "Profesor:\n" + Style.END + "Heider Sánchez")
    print()

    play_sound("celebration.wav")
    print(Style.BOLD + "Próximamente...\n" + Style.END + "Integrales")
    print()
    input("Para finalizar, presione cualquier tecla")
