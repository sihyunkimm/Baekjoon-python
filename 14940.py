import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

matrix = []
q = deque()
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

for row in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
    for i in range(M):
        if matrix[row][i] == 1:
            matrix[row][i] = -1
        elif matrix[row][i] == 2:
            goal = (row, matrix[row].index(2))
            matrix[row][i] = 0

q.append(goal)

value = 1
while q:
    for i in range(len(q)):
        r, c = q.popleft()
        for d in directions:
            nr = r + d[0]
            nc = c + d[1]
            if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == -1:
                matrix[nr][nc] = value
                q.append((nr, nc))
    value += 1


for r in range(N):
    for c in range(M):
        print(matrix[r][c], end=' ')
    print()
