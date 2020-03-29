#   esta funcion pide el input del nombre de la persona,
#   crea un archivo .txt con su nombre y devuelve una tupla,
#   con el nombre de la persona y su puntaje inicial (= 0)


def crear_persona_puntaje(puntaje="0"):
    nombre = input("Ingresa tu usuario UTEC: ")
    with open(nombre + ".txt", "w+") as file:
        score = puntaje
        file.write(score)
    tupla_localizacion = (nombre, score)
    return tupla_localizacion
#   esta funcion reescribe sobre el archivo .txt previo
#   de la persona, cambiando su puntaje al obtenido
#   acabado el juego. Devuelve la misma tupla


def update_persona_puntaje(usuario, puntaje="0"):
    lugar = usuario + ".txt"
    with open(lugar, "w+") as file:
        score = puntaje
        file.write(score)
    tupla_localizacion = (usuario, score)
    return tupla_localizacion

#   esta funcion recibe el diccionario general que almacena
#   el nombre de las personas como key y sus puntajes como value.
#   También recibe la tupla de ubicación. Luego procede a actualizar
#   el ese par (key, value) del diccionario (porque el usuario tiene un
#   nuevo puntaje. Devuelve el diccionario actualizado


def update_dict(dict, tupla):
    key = tupla[0]
    value = tupla[1]
    dict[key] = value
    return dict
#   esta funcion recibe la localizacion del archivo donde se almacena
#   el diccionario general, y tambien recibe el diccionario actualizado.
#   Procede a reemplazar al diccionario antiguo con el actualizado.


def cambiar_txt_dict(file_location, new_dict):
    with open(file_location, "w+") as replace:
        replace.write(str(new_dict))
