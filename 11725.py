import sys
from collections import deque

N = int(input())
parent = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

parent[1] = 1

q = deque()
q.append(1)
while q:
    current = q.popleft()
    for n in graph[current]:
        if parent[n] == 0:
            parent[n] = current
            q.append(n)

for i in range(2, N+1):
    print(parent[i])
