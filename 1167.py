import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

V = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(V):
    input_dq = deque(map(int, input().split()))
    start_node = input_dq.popleft()

    while len(input_dq) > 1:
        node_to = input_dq.popleft()
        weight = input_dq.popleft()
        graph[start_node].append([node_to, weight])


def dfs(current_node, pre_weight, distances):
    for next_node, weight in graph[current_node]:
        if distances[next_node] == -1:
            distances[next_node] = pre_weight + weight
            dfs(next_node, distances[next_node], distances)

def run(start):
    temp = [-1] * (V+1)
    temp[start] = 0
    dfs(start, 0, temp)
    max_dist = max(temp)
    max_node = temp.index(max_dist)
    return max_node, max_dist


far_from_one, _ = run(1)
_, answer = run(far_from_one)

print(answer)
