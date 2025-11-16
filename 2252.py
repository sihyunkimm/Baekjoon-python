import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

shorts = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    front, back = map(int, input().split())
    shorts[back].append(front)

def print_num(n):
    for s in shorts[n]:
        if not visited[s]:
            print_num(s)
    print(n, end=' ')
    visited[n] = True

for i in range(1, N+1):
    if not visited[i]:
        print_num(i)