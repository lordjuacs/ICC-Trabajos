def mayorListaRec(d):
    if len(d) == 1:
        return  d[0]
    else:
        evaluar = d[0]
        if evaluar > mayorListaRec(d[1:]):
            return evaluar
        else:
            return mayorListaRec(d[1:])

lista = [1,3,4,7,1,2]
print("mayor:", mayorListaRec(lista))