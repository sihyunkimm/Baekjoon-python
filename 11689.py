N = int(input())

def prime_factor(n):
    i = 2
    factors = set()

    while i*i <= n:
        if n % i == 0:
            factors.add(i)
            n //= i
        else:
            i += 1

    if n != 1:
        factors.add(n)

    return factors


def eular(n):
    factors = list(prime_factor(n))
    answer = n
    for f in factors:
        answer *= 1 - 1/f

    return int(answer)


print(eular(N))