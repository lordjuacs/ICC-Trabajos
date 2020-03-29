n = int(input())
count = 1
for x in range(n):
    for y in range(n):
        print(count,end="")
        count += 1
        if count > 9:
            count = 1
    print()