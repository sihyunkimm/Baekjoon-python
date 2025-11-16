import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append([child, weight])
    graph[child].append([parent, weight])


def dfs(pre_node, pre_weight, distances):
    for child, weight in graph[pre_node]:
        if distances[child] == -1:
            distances[child] = pre_weight + weight
            dfs(child, distances[child], distances)

def run(start):
    temp = [-1] * (n+1)
    temp[start] = 0
    dfs(start, 0, temp)
    max_dist = max(temp)
    max_node = temp.index(max_dist)
    return max_node, max_dist


far_from_one, _ = run(1)
_, answer = run(far_from_one)

print(answer)