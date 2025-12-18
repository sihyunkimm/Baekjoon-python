from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = list(list(map(int, list(input().rstrip()))) for _ in range(N))
visited = list(list(False for _ in range(M)) for _ in range(N))
g_map = list(list(0 for _ in range(M)) for _ in range(N))
answer = list(list(0 for _ in range(M)) for _ in range(N))
g_cnt = 0
g_value = [0]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(row, col, g_num):
    q = deque()
    q.append((row, col))
    visited[row][col] = True
    cnt = 0
    while q:
        r, c = q.popleft()
        g_map[r][c] = g_num
        cnt += 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 0 and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True
    return cnt
    

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0 and not visited[i][j]:
            g_cnt += 1
            g_value.append(bfs(i, j, g_cnt))

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            g_set = set()
            for d in range(4):
                nr = i + dr[d]
                nc = j + dc[d]
                if 0 <= nr < N and 0 <= nc < M:
                    g_set.add(g_map[nr][nc])
            g_list = list(g_set)
            tmp = 1
            for g in g_list:
                tmp += g_value[g]
            answer[i][j] = tmp % 10

for line in answer:
    for num in line:
        print(num, end='')
    print()