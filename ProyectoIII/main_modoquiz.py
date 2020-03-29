from funcion_juego import *


class Style:
    BOLD = '\033[1m'
    END = '\033[0m'


print(Style.BOLD + "---------- A la Bika dile No ----------" + Style.END)
print("Bienvenido al juego que te ayudará a\n"
      "practicar tus habilidades para resolver\n"
      "derivadas.")
print()
print("Las reglas son simples:\n"
      "✓ Las respuestas se marcan presionando\n"
      "  las teclas " + Style.BOLD + "a"
      + Style.END + ", " + Style.BOLD + "b"
      + Style.END + " o " + Style.BOLD + "c"
      + Style.END + ".\n"
      + "✓ Mientras más rápido respondas,\n"
        "  más puntos obtendrás.\n"
        "✓ Las respuestas incorrectas te\n"
        "  descontarán puntos.\n"
        "✓ Puedes ayudarte de nuestra\n"
        "  calculadora.")
print()
print("☺ Buena suerte ☺")
print()
jugar()
