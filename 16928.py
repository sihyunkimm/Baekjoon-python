from collections import deque

N, M = map(int, input().split())

shortcuts = {}
dists = [101 for _ in range(101)]

for _ in range(N+M):
    s, e = map(int, input().split())
    shortcuts[s] = e

q = deque()
q.append(1)
dist = 1
dists[1] = 0

while q and dists[100] == 101:
    for _ in range(len(q)):
        current = q.popleft()
        for i in range(1,7):
            if current+i <= 100 and dist < dists[current+i] and current+i not in shortcuts:
                dists[current+i] = dist
                q.append(current+i)
            if current+i in shortcuts and dist < dists[shortcuts[current+i]]:
                dists[shortcuts[current+i]] = dist
                q.append(shortcuts[current+i])
    
    dist += 1

print(dists[100])