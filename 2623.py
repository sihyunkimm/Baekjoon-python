import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [set() for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    input_str = input().rstrip()
    input_str = input_str[2:]
    numbers = list(map(int, input_str.split()))
    for i in range(len(numbers) - 1):
        graph[numbers[i+1]].add(numbers[i])

graph = list(map(list, graph))
answer = []

def dfs(n, depth):
    if depth > N:
        print(0)
        exit()

    if visited[n]:
        return
    
    for front in graph[n]:
        dfs(front, depth + 1)

    answer.append(n)
    visited[n] = True
    return

for i in range(1, N+1):
    dfs(i, 1)

for number in answer:
    print(number)