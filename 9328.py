import sys
from collections import deque

input = sys.stdin.readline

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())  # testcase

for _ in range(T):
    max_row, max_col = map(int, input().split())
    m = [list(input().strip()) for _ in range(max_row)]
    keys = set(input().strip())

    visited = [[False for _ in range(max_col)] for _ in range(max_row)]
    answer = 0
    q = deque()
    doors = {}


    def visit(row, col):
        global answer
        current = m[row][col]
        if current == '.':  # .
            q.append((row, col))
            visited[row][col] = True

        elif current == '$':  # $
            answer += 1
            q.append((row, col))
            visited[row][col] = True

        elif current.islower():  # key
            keys.add(current)
            q.append((row, col))
            visited[row][col] = True
            if current.upper() in doors:
                for r, c in doors[current.upper()]:
                    q.append((r, c))
                    visited[r][c] = True

        elif current.isupper():  # door
            if current in doors:
                doors[current].append((row, col))
            else:
                doors[current] = [(row, col)]

            if current.lower() in keys:
                q.append((row, col))
                visited[row][col] = True

        else:  # *
            pass
    
    
    for row in range(max_row):
        for col in range(max_col):
            if row == 0 or row == max_row-1 or col == 0 or col == max_col-1:
                visit(row, col)

    while q:
        row, col = q.popleft()
        for d in range(4):
            cur_row, cur_col = row + dr[d], col + dc[d]
            if 0 <= cur_row < max_row and 0 <= cur_col < max_col and not visited[cur_row][cur_col]:
                visit(cur_row, cur_col)

    print(answer)
