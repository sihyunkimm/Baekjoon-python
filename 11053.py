N = int(input())
A = list(map(int, input().split()))
length = [1]

for i in range(1, N):
    max_len = 1
    for j in range(i):
        if A[j] < A[i] and length[j] >= max_len:
            max_len = length[j] + 1
    length.append(max_len)

print(max(length))
