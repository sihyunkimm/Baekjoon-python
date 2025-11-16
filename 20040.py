import sys

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n)]

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    parent_x = find(x)
    parent_y = find(y)
    if parent_x < parent_y:
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y

answer = 0
for i in range(1, m+1):
    x, y = map(int, input().split())
    if find(x) == find(y):
        answer = i
        break
    union(x, y)
    
print(answer)
