import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

forward_graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]
edge_count = [0 for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    forward_graph[u].append((v, w))
    reverse_graph[v].append((u, w))
    edge_count[v] += 1

start, end = map(int, input().split())

longest_dist = [0 for _ in range(N+1)]
queue = deque()
for node in range(1, N+1):
    if edge_count[node] == 0:
        queue.append(node)

while queue:
    cur = queue.popleft()
    for next, weight in forward_graph[cur]:
        if longest_dist[next] < longest_dist[cur] + weight:
            longest_dist[next] = longest_dist[cur] + weight
        edge_count[next] -= 1
        if edge_count[next] == 0:
            queue.append(next)

max_dist = longest_dist[end]

golden = 0
visited = [False for _ in range(N+1)]
queue = deque([end])
visited[end] = True

while queue:
    cur = queue.popleft()
    for prev, weight in reverse_graph[cur]:
        if longest_dist[prev] + weight == longest_dist[cur]:
            golden += 1
            if not visited[prev]:
                visited[prev] = True
                queue.append(prev)

print(max_dist)
print(golden)