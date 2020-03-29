def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def comb(N,k):
    return (fact(N) // (fact(k) * fact(N - k)))

N = int(input("N: "))
k = int(input("k: "))
print("Grupos distintos:",comb(N,k))
