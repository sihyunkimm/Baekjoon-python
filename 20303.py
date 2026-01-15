import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

candy = [0]
candy.extend(list(map(int, input().split())))

parent = [i for i in range(N+1)]
def find(x):  
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]  

def union(x, y):
    x, y = find(x), find(y)
    if x < y: 
        parent[y] = x
    else:
        parent[x] = y
        

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

WEIGHT = 0
VALUE = 1
weight_value = [[0, 0] for _ in range(N+1)]
for i in range(1, N+1):
    p = find(i)
    weight_value[p][WEIGHT] += 1
    weight_value[p][VALUE] += candy[i]

weight_value.sort() # 앞에 [0,0]이 많이 생기는 구조인데 고치기 귀찮다

backpack = [[0 for _ in range(K)] for _ in range(N+1)]
for g in range(1, N+1):
    for w in range(1, K):
        cur_weight = weight_value[g][WEIGHT]
        if cur_weight <= w:
            backpack[g][w] = max(backpack[g-1][w], weight_value[g][VALUE] + backpack[g-1][w - cur_weight])
        else:
            backpack[g][w] = backpack[g-1][w]

print(backpack[-1][-1])

