import sys
input = sys.stdin.readline

N, E = map(int, input().split())
INF = float('inf')
graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
for i in range(N+1):
    graph[i][i] = 0
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)
v1, v2 = map(int, input().split())

def dajkstra(start, end):
    visited = [False for _ in range(N+1)]
    visited[start] = True
    for _ in range(N):
        min_dist = INF
        min_node = -1
        for i in range(1, N+1):
            if not visited[i] and graph[start][i] < min_dist:
                min_node = i
                min_dist = graph[start][i]
        if min_dist == INF:
            break
        visited[min_node] = True
        for i in range(1, N+1):
            if not visited[i]:
                graph[start][i] = min(graph[start][i], min_dist + graph[min_node][i])
    return graph[start][end]

case1 = dajkstra(1, v1) + dajkstra(v1, v2) + dajkstra(v2, N)
case2 = dajkstra(1, v2) + dajkstra(v2, v1) + dajkstra(v1, N)

if case1 == INF and case2 == INF:
    print(-1)
else:
    print(min(case1, case2))
