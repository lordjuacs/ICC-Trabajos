count = 0
sum = 0
while True:
    x = int(input("num" + str(count) + ": "))
    if x >= 0:
        sum = sum + x
        count = count + 1
        if x == 0:
            count = count - 1
            print(sum/count)
            break
    else:
        print("error")
        break