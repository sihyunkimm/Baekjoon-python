from collections import deque

MAX = 100000


N, M = map(int, input().split())

dstN = [-1 for _ in range(MAX+1)]
dstN[N] = 0
q = deque()
q.append(N)

while q:
    current = q.popleft()
        
    if current*2 <= MAX and dstN[current*2] == -1:
        dstN[current*2] = dstN[current]
        q.append(current*2)
        
    if current > 0 and dstN[current-1] == -1:
        dstN[current-1] = dstN[current] + 1
        q.append(current-1)
        
    if current < MAX and dstN[current+1] == -1:
        dstN[current+1] = dstN[current] + 1
        q.append(current+1)

print(dstN[M])
