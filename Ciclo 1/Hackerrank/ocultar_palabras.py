def largest_element(frase_lista):
    max = 0
    for element in frase_lista:
        length = len(element)
        if length > max:
            max = length
    return max

frase = input()
frase_lista = frase.split()
nueva_lista = []
union = ""
palabra_grande = largest_element(frase_lista)

for element in frase_lista:
    if len(element) < palabra_grande or len(element) == palabra_grande:
        element += "@" * (palabra_grande-len(element))
        new_element = element
        nueva_lista.append(new_element)

count_letter = 0

for new_element in nueva_lista:
    for new_element in nueva_lista:
        for new_element in nueva_lista:
            if count_letter not in range(len(new_element)):
                break
            union += new_element[count_letter]
        count_letter += 1
        print(union,end=" ")
        union = ""