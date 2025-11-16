import sys

input = sys.stdin.readline
INF = float('inf')

number_nodes = int(input())
number_lines = int(input())

graph = [[INF for _ in range(number_nodes + 1)] for _ in range(number_nodes + 1)]
for i in range(1, number_nodes + 1):
    graph[i][i] = 0

for _ in range(number_lines):
    start, end, cost = map(int, input().split())
    if cost < graph[start][end]:
        graph[start][end] = cost

for k in range(number_nodes+1):
    for i in range(number_nodes+1):
        for j in range(number_nodes+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, number_nodes + 1):
    for j in range(1, number_nodes + 1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

