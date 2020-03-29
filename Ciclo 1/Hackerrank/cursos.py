curso_a = input().split(",")
curso_b = input().split(",")
ambos = []
for element in curso_a:
    if element in curso_b:
        ambos.append(element)
ambos.sort()
for i in ambos:
    print(i)