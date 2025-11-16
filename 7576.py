import sys
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

M, N= map(int, sys.stdin.readline().strip().split())

box = []
for _ in range(N):
  box.append(list(map(int, sys.stdin.readline().strip().split())))

new_riped = deque()

for r in range(N):
  for c in range(M):
    if box[r][c] == 1:
      new_riped.append([r, c])

while new_riped:
  for _ in range(len(new_riped)):
    r, c = new_riped.popleft()

    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]

      if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0:
        box[nr][nc] = box[r][c] + 1
        new_riped.append([nr, nc])
        
day = 0

for row in box:
  for tomato in row:
    if tomato == 0:
      print(-1)
      exit(0)
  day = max(day, max(row))

# 0일차에 익은 토마토가 1이므로 -1
print(day - 1)