n = int(input())
m = int(input())
count = 1
for x in range(n):
    for y in range(m):
        if count % 3 != 0:
            print(count,end="\t")
            count += 1
        else:
            print("X", end="\t")
            count += 1
    print()
