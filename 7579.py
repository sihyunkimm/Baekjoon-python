import sys

input = sys.stdin.readline
NULL = -1
COST = 0
MEM = 1

N, M = map(int, input().split())
mems = list(map(int, input().split()))
costs = list(map(int, input().split()))

apps = [[costs[i], mems[i]] for i in range(N)]
apps.sort()

while apps and apps[0][0] == 0:
    M -= apps[0][1]
    N -= 1
    apps = apps[1:]

temp = [[NULL, NULL]]
temp.extend(apps)
apps = temp

if M <= 0:
    print(0)
    exit()

cost_sum = sum(costs)
dp = [[NULL for _ in range(cost_sum + 1)] for _ in range(N + 1)]

dp[0] = [0 for _ in range(cost_sum + 1)]
for i in range(N + 1):
    dp[i][0] = 0

for cur_app in range(1, N + 1):
    for cur_cost in range(1, cost_sum + 1):
        if apps[cur_app][COST] > cur_cost:
            dp[cur_app][cur_cost] = dp[cur_app - 1][cur_cost]
        else:
            dp[cur_app][cur_cost] = max(dp[cur_app - 1][cur_cost], apps[cur_app][MEM] + dp[cur_app - 1][cur_cost - apps[cur_app][COST]])

for cost in range(1, cost_sum + 1):
    for i in range(1, N + 1):
        if dp[i][cost] >= M:
            print(cost)
            exit()