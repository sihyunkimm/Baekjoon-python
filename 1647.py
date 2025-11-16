import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

parent = [i for i in range(N+1)]

def find(n):
    while n != parent[n]:
        n = parent[n]
    return n

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a < parent_b:
        parent[parent_b] = a
    else:
        parent[parent_a] = b

lines = []

for _ in range(M):
    a, b, c = map(int, input().split())
    heapq.heappush(lines, [c, a, b])

cnt = 0
cost_sum = 0
last_cost = 0
while cnt < N-1:
    c, a, b = heapq.heappop(lines)
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        cost_sum += c
        last_cost = c

print(cost_sum - last_cost)