import sys
from heapq import *

input = sys.stdin.readline
INF = float('inf')

N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

def dajkstra(start):
    distance = [INF] * (N+1)
    q = []

    distance[start] = 0
    heappush(q, (0, start))
        
    while q:
        cost_now, node_now = heappop(q)

        if cost_now > distance[node_now]:
            continue
        
        for node_to, cost_to in graph[node_now]:
            if cost_now + cost_to < distance[node_to]:
                distance[node_to] = cost_now + cost_to
                heappush(q, (cost_now + cost_to, node_to))

    return distance


students = []

for i in range(1, N+1):
    to_x = dajkstra(i)[X]
    from_x = dajkstra(X)[i]
    students.append(to_x + from_x)

print(max(students))