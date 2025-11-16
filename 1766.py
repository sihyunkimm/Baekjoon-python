import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

answer = []
graph = [[] for _ in range(N+1)]
depth = [0 for _ in range(N+1)]
queue = []

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    depth[b] += 1

for i in range(1, N+1):
    if depth[i] == 0:
        heapq.heappush(queue, i)

while queue:
    temp = heapq.heappop(queue)
    answer.append(temp)
    for i in graph[temp]:
        depth[i] -= 1
        if depth[i] == 0:
            heapq.heappush(queue, i)

print(*answer)