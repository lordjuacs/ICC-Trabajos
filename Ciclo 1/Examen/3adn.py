print("input:")
primaria = input()
secundaria = []
for i in primaria:
    if i == "a":
        secundaria.append("t")
    elif i == "t":
        secundaria.append("a")
    elif i == "g":
        secundaria.append("c")
    else:
        secundaria.append("g")
print("output:")
print("".join(secundaria))