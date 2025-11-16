import sys
from copy import deepcopy
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
board = list(list(map(int, input().split())) for _ in range(N))

def print_board():
    for line in board:
        print(*line)

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
U, D, L, R = 0, 1, 2, 3

def move(cur_board, dir):
    visited = [list(False for _ in range(N)) for _ in range(N)]
    # 상, 좌
    if dir == U or dir == L:
        row, col = 0, 0
        while row < N:
            if cur_board[row][col] != 0:
                nr, nc = row, col
                while True:
                    nr += dr[dir]
                    nc += dc[dir]
                    if not (0 <= nr < N and 0 <= nc < N) or cur_board[nr][nc] != 0:
                        break

                isOutOfRange = False      
                if nr < 0:
                    nr += 1
                    isOutOfRange = True
                elif nc < 0:
                    nc +=  1
                    isOutOfRange = True

                if nr == row and nc == col:
                    pass
                elif isOutOfRange:
                    cur_board[nr][nc] = cur_board[row][col]
                    cur_board[row][col] = 0
                elif cur_board[nr][nc] == cur_board[row][col] and not visited[nr][nc]:
                    cur_board[nr][nc] *= 2
                    cur_board[row][col] = 0
                    visited[nr][nc] = True
                else:
                    nr -= dr[dir]
                    nc -= dc[dir]
                    if not (nr == row and nc == col):
                        cur_board[nr][nc] = cur_board[row][col]
                        cur_board[row][col] = 0

            row += (col+1) // N
            col = (col+1) % N

    # 하, 우
    else:
        row, col = N-1, N-1
        while row >= 0:
            if cur_board[row][col] != 0:
                nr, nc = row, col
                while True:
                    nr += dr[dir]
                    nc += dc[dir]
                    if not (0 <= nr < N and 0 <= nc < N) or cur_board[nr][nc] != 0:
                        break

                isOutOfRange = False      
                if nr >= N:
                    nr -= 1
                    isOutOfRange = True
                elif nc >= N:
                    nc -=  1
                    isOutOfRange = True

                if nr == row and nc == col:
                    pass
                elif isOutOfRange:
                    cur_board[nr][nc] = cur_board[row][col]
                    cur_board[row][col] = 0
                elif cur_board[nr][nc] == cur_board[row][col] and not visited[nr][nc]:
                    cur_board[nr][nc] *= 2
                    cur_board[row][col] = 0
                    visited[nr][nc] = True
                else:
                    nr -= dr[dir]
                    nc -= dc[dir]
                    if not (nr == row and nc == col):
                        cur_board[nr][nc] = cur_board[row][col]
                        cur_board[row][col] = 0

            col -= 1
            if col < 0:
                row -= 1
                col = N-1


answer = 0
def backtest(cur_board, move_cnt):
    global answer
    if move_cnt >= 5:
        for i in range(N):
            for j in range(N):
                answer = max(answer, cur_board[i][j])
        return
    for dir in range(4):
        tmp_board = deepcopy(cur_board)
        move(tmp_board, dir)
        backtest(tmp_board, move_cnt+1)


backtest(board, 0)
print(answer)