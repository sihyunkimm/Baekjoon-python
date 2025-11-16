import sys

input = sys.stdin.readline
COST = 0
VALUE = 1

goal_customer, total_city = map(int, input().split())

cities = []
for _ in range(total_city):
    cost, value = map(int, input().split())
    cities.append((cost, value))
cities.sort(key = lambda x: x[VALUE] / x[COST])

maximum_cost = (goal_customer // cities[0][VALUE] + 1) * cities[0][COST]
dp = [[0 for _ in range(maximum_cost + 1)] for _ in range(total_city + 1)]

cities = [(0, 0)] + cities
for cur_city in range(1, total_city + 1):
    for cur_cost in range(1, maximum_cost + 1):
        if cities[cur_city][COST] <= cur_cost:
            dp[cur_city][cur_cost] = max(dp[cur_city - 1][cur_cost], cities[cur_city][VALUE] + dp[cur_city][cur_cost - cities[cur_city][COST]]) #넣었을 때 넣은 가치 + 넣기 전 최대값
        else:
            dp[cur_city][cur_cost] = dp[cur_city - 1][cur_cost]

for i in range(maximum_cost + 1):
    for j in range(total_city + 1):
        if dp[j][i] >= goal_customer:
            print(i)
            exit(0)