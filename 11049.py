import sys

input = sys.stdin.readline
MAX_VALUE = 2**31 - 1

N = int(input())

matrixs = [list(map(int, input().split())) for _ in range(N)]

dp = [[MAX_VALUE for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[i][i] = 0

for i in range(N-1):
    dp[i][i+1] = matrixs[i][0] * matrixs[i][1] * matrixs[i+1][1]

for interval in range(1, N):
    for start in range(N):
        end = start + interval
        if end >= N:
            continue

        for k in range(start, end):
            dp[start][end] = min( dp[start][end], dp[start][k] + dp[k+1][end] + matrixs[start][0] * matrixs[k][1] * matrixs[end][1] )

print(dp[0][N-1])