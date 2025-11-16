from collections import deque

N = int(input())

# index : row, value : col 
placed_col = [0 for _ in range(N)]
count = 0

def canPlace(row):
    for i in range(row):
        if placed_col[row] == placed_col[i] or abs(row - i) == abs(placed_col[row] - placed_col[i]):
            return False
    return True

def backtrack(current_row):
    global count
    if current_row == N:
        count += 1
    else:
        for i in range(N):
            placed_col[current_row] = i
            if canPlace(current_row):
                backtrack(current_row + 1)

backtrack(0)
print(count)
