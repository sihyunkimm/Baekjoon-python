import sys
from heapq import heappop, heappush
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]


for _ in range(M):
    a, b = map(int, input().split())
    # heappush(graph[a], b)
    # heappush(graph[b], a)
    graph[a].append(b)
    graph[b].append(a)


for i in range(1, N+1):
    graph[i].sort()


visited_d = [False for _ in range(N+1)]
def dfs(n):
    if visited_d[n]:
        return
    
    print(n, end=' ')
    visited_d[n] = True

    for i in graph[n]:
        dfs(i)


visited_b = [False] * (N+1)
q = deque()
q.append(V)
def bfs():
    while q:
        n = q.popleft()
        if not visited_b[n]:
            print(n, end=' ')
            visited_b[n] = True
        for c in graph[n]:
            if not visited_b[c]:                
                q.append(c)


dfs(V)
print()
bfs()