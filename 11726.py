n = int(input())

cases = {
    1: 1,
    2: 2
}

for i in range(3, n+1):
    cases[i] = cases[i-1] + cases[i-2]

print(cases[n] % 10007)
