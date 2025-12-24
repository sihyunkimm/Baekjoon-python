R, C = map(int, input().split())
board = list(list(input()) for _ in range(R))
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


past = set()
past.add(board[0][0])
answer = 1
def back(r, c):
    global answer
    answer = max(answer, len(past))
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in past:
            past.add(board[nr][nc])
            back(nr, nc)
            past.remove(board[nr][nc])

back(0, 0)
print(answer)