count = 1
sum = 0
x =
if x >= 0:
    while x != 0:
        x = int(input("x" + str(count)))
        sum = sum + x
        count = count + 1
        prom = float(sum / count)
    if x == 0:
            print(prom)
else:
    print("error")