import sys
sys.setrecursionlimit(10000)

def dfs(n, visited, graph):
    visited[n] = True
    for i in graph[n]:
        if visited[i] == False:
            dfs(i, visited, graph)


N, M = map(int, sys.stdin.readline().split())

visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


count = 0
for i in range(1, N+1):
    if visited[i] == False:
        dfs(i, visited, graph)
        count += 1

print(count)
