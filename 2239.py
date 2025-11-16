import sys

input = sys.stdin.readline

sudoku = [list(map(int, list(input().rstrip()))) for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeros.append((i, j))


def is_possible(row, col, number):
    for i in range(9):
        if sudoku[row][i] == number:
            return False
        if sudoku[i][col] == number:
            return False
        
    for r in range(3):
        for c in range(3):
            if sudoku[r + (row // 3) * 3][c + (col // 3) * 3] == number:
                return False
            
    return True


def backtrack(count):
    if count == len(zeros):
        for line in sudoku:
            print(''.join(map(str, line)))
        exit()
        
    row, col = zeros[count]
    for i in range(1, 10):
        if is_possible(row, col, i):            
            sudoku[row][col] = i
            backtrack(count + 1)
            sudoku[row][col] = 0

backtrack(0)