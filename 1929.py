import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            return False            
    return True


M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)
