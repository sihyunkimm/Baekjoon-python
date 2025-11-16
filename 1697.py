from collections import deque

MAX = 10**6

n, k = map(int, input().split())


visited = [0] * (MAX+1)

q = deque()
q.append(n)

while q:
    cur = q.popleft()
    if cur == k:
        break
    for i in (cur+1, cur-1, cur*2):
        if 0 <= i <= MAX and not visited[i]: 
          visited[i] = visited[cur] + 1
          q.append(i)

print(visited[k])
