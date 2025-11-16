import sys
from collections import deque

# up, down, front, back, right, left
dh = [1, -1, 0, 0, 0, 0]
dr = [0, 0, 1, -1, 0, 0]
dc = [0, 0, 0, 0, 1, -1]
NUM_OF_DIRECTIONS = 6

M, N, H = map(int, sys.stdin.readline().split())

# height, row, col
matrix = []
for i in range(H):
    matrix.append([])
    for j in range(N):
        matrix[i].append(list(map(int, sys.stdin.readline().split())))

q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 1:
                q.append((i, j, k))

date = 1
while q:
    date += 1
    for _ in range(len(q)):
        h, r, c = q.popleft()
        for i in range(NUM_OF_DIRECTIONS):
            nh = h + dh[i]
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and matrix[nh][nr][nc] == 0:
                matrix[nh][nr][nc] = date
                q.append((nh, nr, nc))
    

    
for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 0:
                print(-1)
                exit()
print(date-2)
