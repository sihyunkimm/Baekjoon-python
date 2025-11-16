N = int(input())
foods = list(map(int, input().split()))
foods.sort()

answer = 0
for i in range(N-1):
    for j in range(i+1, N):
        answer += (foods[j]-foods[i]) * 2**(j-i-1)
        answer %= 1_000_000_007

print(answer)