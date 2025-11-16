import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 우상향 대각선 (row + col 이 일정, 0 <= row+col <= 2N-1, diag_up[row + col])
diag_up = [False for _ in range(2*N-1)]
# 우하향 대각선 (row - col 이 일정, -(N-1) <= row-col <= N-1 , diag_down[N-1 + row - col])
diag_down = [False for _ in range(2*N-1)]

max_bishop = [0, 0]  # [흑, 백]

def backtrack(idx, cnt, color, cell_list):
    """
    idx: cell_list에서 현재 탐색할 인덱스
    cnt: 현재까지 놓은 비숍 개수
    color: 0(흑), 1(백)
    cell_list: 해당 색의 비숍을 놓을 수 있는 좌표 리스트
    """
    if idx == len(cell_list):
        max_bishop[color] = max(max_bishop[color], cnt)
        return
    
    row, col = cell_list[idx]
    if not diag_up[row+col] and not diag_down[N-1 + row-col]:
        diag_up[row+col] = True
        diag_down[N-1 + row-col] = True
        backtrack(idx+1, cnt+1, color, cell_list)
        diag_up[row+col] = False
        diag_down[N-1 + row-col] = False
        
    backtrack(idx+1, cnt, color, cell_list)

black_cells = []  # (i+j)%2==0 흑
white_cells = []  # (i+j)%2==1 백
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            if (i+j)%2 == 0:
                black_cells.append((i, j))
            else:
                white_cells.append((i, j))

backtrack(0, 0, 0, black_cells)
backtrack(0, 0, 1, white_cells)
print(max_bishop[0] + max_bishop[1])