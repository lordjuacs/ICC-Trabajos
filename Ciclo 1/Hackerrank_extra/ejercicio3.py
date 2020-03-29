def stacking(lista):
    size = len(lista)
    nueva = []
    se_puede = True
    left = 0
    right = 1
    for i in range(size//2):
        while left < right:
            if i % 2 == 0:
                nueva.append(lista[left])
                if len(nueva) > 1 and nueva[-1] > nueva[-2]:
                    se_puede == False
                    break
                left += 1

            else:
                nueva.append(lista[-right])
                if len(nueva) > 1 and nueva[-1] > nueva[-2]:
                    se_puede == False
                    break
                right += 1
    print(nueva)
    return se_puede



valores = []
cases = int(input())
for i in range(cases):
    tamano = int(input())
    cubos = input().split(" ")
    cubos = [int(i) for i in cubos]
    valor = stacking(cubos)
    if valor == True:
        valores.append("Yes")
    else:
        valores.append("NO")


for i in valores:
    print(i)