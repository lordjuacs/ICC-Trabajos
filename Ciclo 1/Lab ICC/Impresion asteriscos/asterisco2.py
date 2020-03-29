n = int(input())
for x in range(n):
    for y in range(n-1-x):
        print(" ",end=" ")
    for y in range(x+1):
        print("#",end=" ")
    print()
print()
for x in range(n):
    for y in range(x):
        print(" ",end=" ")
    for y in range(n-x):
        print("#",end=" ")
    print()