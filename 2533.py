import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
dp = [[0,1] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n):
    visited[n] = True
    for next in graph[n]: 
        if(visited[next]): continue 
        dfs(next) 
        dp[n][0]+=dp[next][1] 
        dp[n][1]+=min(dp[next])

dfs(1) 
print(min(dp[1]))