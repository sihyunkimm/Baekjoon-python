import sys
input = sys.stdin.readline
INF = float('inf')

N = int(input())
M = int(input())

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for i in range(N+1):
    graph[i][i] = 0

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s][e] = min(graph[s][e], w)

def dajkstra(start):
    visited = [False for _ in range(N+1)]
    visited[start] = True  

    for _ in range(N):
        min_idx = -1
        min_dis = INF
        for i in range(1, N+1):
            if not visited[i] and graph[start][i] < min_dis:
                min_idx = i
                min_dis = graph[start][i]

        if min_idx == -1:
            break
        
        for i in range(1, N+1):
            graph[start][i] = min(graph[start][i], graph[start][min_idx] + graph[min_idx][i])
        
        visited[min_idx] = True


start, end = map(int, input().split())
dajkstra(start)
print(graph[start][end])