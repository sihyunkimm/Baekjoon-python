import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(input().rstrip()))


def searchNotVisited(visited):
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                return (r, c)
            
    return False


def bfs():
    visited = [[False for _ in range(N)] for _ in range(N)]
    
    cnt = 0
    start = (0, 0)

    while start:
        cnt += 1
        q = deque()
        q.append(start)
        cur_color = matrix[start[0]][start[1]]
        visited[start[0]][start[1]] = True
        
        while q:
            cr, cc = q.popleft()            
            for d in range(4):
                nr = cr + dr[d]
                nc = cc + dc[d]
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and matrix[nr][nc] == cur_color:
                    q.append((nr, nc))
                    visited[nr][nc] = True

        start = searchNotVisited(visited)

    return cnt


normal = bfs()

for r in range(N):
    for c in range(N):
        if matrix[r][c] == 'G':
            matrix[r][c] = 'R'

blind = bfs()

print(normal, blind)