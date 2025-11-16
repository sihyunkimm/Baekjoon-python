import sys

input = sys.stdin.readline
INF = float('inf')
R, G, B = 0, 1, 2

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
answer = INF

for start_rgb in range(3):
    dp = [[INF, INF, INF] for _ in range(N)]
    dp[0][start_rgb] = costs[0][start_rgb] 

    for i in range(1, N):
        dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + costs[i][R] 
        dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + costs[i][G]
        dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + costs[i][B]

    dp[-1][start_rgb] = INF
    answer = min(answer, min(dp[-1])) 

print(answer)