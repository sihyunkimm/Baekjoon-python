import sys

N, M = map(int, sys.stdin.readline().split())

board = []
for i in range(N):
    board.append(sys.stdin.readline().rstrip())
    
ans = N*M

for i in range(N-7):
    for j in range(M-7):
        wstart = 0
        bstart = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != 'W':
                        wstart += 1
                    if board[k][l] != 'B':
                        bstart += 1
                else:
                    if board[k][l] != 'B':
                        wstart += 1
                    if board[k][l] != 'W':
                        bstart += 1
        ans = min(ans, wstart, bstart)

print(ans)
