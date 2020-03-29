import winsound
# se importa esta libreria para poder ejecutar sonidos


def play_sound(file_name):
    winsound.PlaySound(file_name, winsound.SND_ASYNC)
