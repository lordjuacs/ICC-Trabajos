# method to find sum of digits
# of a number until sum becomes
# single digit
def superDigit(n):
    sum = 0
    while (n > 0 or sum > 9):
        if (n == 0):
            n = sum
            sum = 0
        sum += n % 10
        n /= 10

    return sum


(n, k) = input().split(" ")
k = int(n)
p = int(n * k)
print(superDigit(p))