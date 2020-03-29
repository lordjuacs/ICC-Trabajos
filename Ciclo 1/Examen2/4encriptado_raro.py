total = int(input())
dic = {}
for i in range(total):
    key = input()
    valor = input()
    dic[key] = valor

print("Claves:", " ".join(dic))
print("Valores:", end=" ")
for i in dic:
    print(dic[i], end=" ")
print()

texto = input()
u = ""
for i in texto:
    if i in dic:
        u += dic[i]
    else:
        u += "#"
print(u)
