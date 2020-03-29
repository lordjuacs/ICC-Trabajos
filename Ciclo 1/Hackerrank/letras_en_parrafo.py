parrafo = str(input())
letra1 = str(input())
letra2 = str(input())
count1 = 0
count2 = 0
for i in parrafo:
    if i == letra1:
        count1 += 1
    elif i == letra2:
        count2 += 1
print(count1)
print(count2)
