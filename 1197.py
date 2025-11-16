import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)


V, E = map(int, input().split())

edges = [] # [weight, a, b]
for _ in range(E):
    a, b, w = map(int, input().split())
    edges.append([w, a, b])

edges.sort()


# union-find
parent = [i for i in range(V+1)]

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def is_same_parent(a, b):
    return get_parent(a) == get_parent(b)


answer = 0
for weight, a, b in edges:
    if not is_same_parent(a, b):
        union_parent(a, b)
        answer += weight
    

print(answer)