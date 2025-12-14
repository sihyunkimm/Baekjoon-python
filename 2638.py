from collections import deque
N, M = map(int, input().split())
matrix = list(list(map(int, input().split())) for _ in range(N))
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
answer = 0

def checkCheese():
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                return True
    return False

isCheese = checkCheese()
while isCheese:
    value = list(list(0 for _ in range(M)) for _ in range(N))
    visited = list(list(False for _ in range(M)) for _ in range(N))

    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == False:
                if matrix[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                else:
                    value[nr][nc] += 1
                

    for i in range(N):
        for j in range(M):
            if value[i][j] >= 2:
                matrix[i][j] = 0
    answer += 1
    isCheese = checkCheese()

print(answer)