import sys
input = sys.stdin.readline

R, C = map(int, input().split())
matrix = [list(map(int, list(input().strip()))) for _ in range(R)]

rd, ld, ru, lu, dpd, dpu = ([[0]*C for _ in range(R)] for _ in range(6))


for r in range(R):
    for c in range(C):
        if matrix[r][c] == 1:
            cnt, nr, nc = 0, r, c
            while 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] == 1:
                cnt+=1
                nr+=1
                nc+=1
            rd[r][c] = cnt

            cnt, nr, nc = 0, r, c
            while 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] == 1:
                cnt+=1
                nr+=1
                nc-=1
            ld[r][c] = cnt

            cnt, nr, nc = 0, r, c
            while 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] == 1:
                cnt+=1
                nr-=1
                nc+=1
            ru[r][c] = cnt

            cnt, nr, nc = 0, r, c
            while 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] == 1:
                cnt+=1
                nr-=1
                nc-=1
            lu[r][c] = cnt

answer = 0
for r in range(R):
    for c in range(C):
        dpd[r][c] = min(rd[r][c], ld[r][c])
        dpu[r][c] = min(ru[r][c], lu[r][c])

for r in range(R):
    for c in range(C):
        upper_shell = dpd[r][c]
        for cur_size in range(upper_shell, -1, -1):
            nr = r + (cur_size-1) * 2
            if r <= nr < R and dpu[nr][c] >= cur_size:
                answer = max(answer, cur_size)

print(answer)
        


"""
시간초과
def is_dia(r, c, size):
    for i in range(size):
        left =  size-(i+1) +1 -1    # 왼쪽 빈칸 개수 + 다음자리 - 인덱스 변환
        right = size*2-1 - (size-(i+1)) -1   # 끝 - 오른쪽 빈칸 개수 - 인덱스변환
        if not (matrix[r+i][c + left] == 1 and matrix[r+i][c + right] == 1):  
            return False
    for i in range(size-1):
        left = size-(size-1-i) +1 -1
        right = size*2-1-(size-(size-1-i)) -1
        if not (matrix[r+size+i][c + left] == 1 and matrix[r+size+i][c + right] == 1):
            return False
    return True

def is_mine(size):
    total_size = 2*size - 1
    for r in range(R-total_size + 1):
        for c in range(C-total_size + 1):
            if is_dia(r, c, size):
                return True
    return False


min_edge = min(R, C)
if min_edge % 2 == 0:
    for size in range(min_edge//2, -1, -1):
        if is_mine(size):
            print(size)
            break            
else:
    for size in range(min_edge//2+1, -1, -1):
        if is_mine(size):
            print(size)
            break
"""