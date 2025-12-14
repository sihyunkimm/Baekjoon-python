INF = 10 ** 9

orders = list(map(int, input().split()))
orders.pop()

def cost(cur, nxt):
    if cur == nxt:
        return 1
    if cur == 0:
        return 2
    if abs(cur - nxt) == 2:
        return 4
    return 3

dp = [[INF] * 5 for _ in range(5)] # dp[왼발][오른발] = 총비용
dp[0][0] = 0

for cmd in orders:
    new_dp = [[INF] * 5 for _ in range(5)]
    for l in range(5):
        for r in range(5):
            if dp[l][r] == INF:
                continue
            new_dp[cmd][r] = min(new_dp[cmd][r], dp[l][r] + cost(l, cmd))
            new_dp[l][cmd] = min(new_dp[l][cmd], dp[l][r] + cost(r, cmd))
    dp = new_dp

answer = min(min(row) for row in dp)
print(answer)