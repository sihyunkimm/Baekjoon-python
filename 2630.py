def isFill(r, c, size):
    b = matrix[r][c]
    for i in range(size):
        for j in range(size):
            if matrix[r+i][c+j] != b:
                return False
    return True

#정사각형 개수만 세는 문제인줄 알았다가 나중에 수정
def dncZero(r, c, size):
    if isFill(r, c, size):
        if matrix[r][c] == 0:
            return 1
        else:
            return 0
    else:
        return dncZero(r, c, size//2) + dncZero(r, c+size//2, size//2) + dncZero(r+size//2, c, size//2) + dncZero(r+size//2, c+size//2, size//2)

def dncOne(r, c, size):
    if isFill(r, c, size):
        if matrix[r][c] == 0:
            return 0
        else:
            return 1
    else:
        return dncOne(r, c, size//2) + dncOne(r, c+size//2, size//2) + dncOne(r+size//2, c, size//2) + dncOne(r+size//2, c+size//2, size//2)


n = int(input())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

print(dncZero(0, 0, n))
print(dncOne(0, 0, n))
