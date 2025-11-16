N = int(input())
counts = [0 for _ in range(10)]
tens = 1

while N > 0:
    while N % 10 != 9:
        for i in str(N):
            counts[int(i)] += tens
        N -= 1

    if N >= 10:
        for i in range(10):
            counts[i] += (N // 10 + 1) * tens        
    else:
        for i in range(N + 1):
            counts[i] += tens

    counts[0] -= tens
    tens *= 10
    N //= 10

print(*counts)