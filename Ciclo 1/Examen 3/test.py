def major(matriz):
    if len(matriz) == 1:
        return matriz[0]
    else:
        alumno = matriz[0]
        if sum(alumno) > sum(major(matriz[1:])):
            return alumno
        else:
            return major(matriz[1:])



matriz = [[1,2,3], [4,5,6], [7,8,9]]
print("Mejor alumno:", major(matriz))