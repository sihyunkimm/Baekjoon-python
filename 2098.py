import sys

input = sys.stdin.readline
INF = float('inf')
NULL = -1

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[NULL for _ in range(1 << N)] for _ in range(N)]

def dfs(cur, visited):
    if visited == (1 << N) - 1:
        if graph[cur][0]:
            return graph[cur][0]
        else:
            return INF
        
    if dp[cur][visited] != NULL:
        return dp[cur][visited]
    
    min_value = INF
    for i in range(1, N):          
        if graph[cur][i] == 0:         
            continue
        if visited & (1 << i):
            continue
        
        min_value = min(min_value, dfs(i, visited | (1 << i)) + graph[cur][i])
    dp[cur][visited] = min_value

    return dp[cur][visited]

print(dfs(0, 1))