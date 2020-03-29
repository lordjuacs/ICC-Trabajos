import math
def calcCombin(N,k):
    return int((math.factorial(N))/((math.factorial(k)) * math.factorial(N - k)))

N = int(input("N: "))
k = int(input("k: "))
factorial = calcCombin(N,k)
print("Grupos distintos:",factorial)
