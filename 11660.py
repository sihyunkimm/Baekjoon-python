import sys

N, M = map(int, sys.stdin.readline().split())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

sums = [[]]

k = 0
for i in matrix[0]:
    k += i
    sums[0].append(k)

for i in range(1, N):
    sums.append([matrix[i][0] + sums[i-1][0]])
    for j in range(1, N):
        sums[i].append(matrix[i][j] + sums[i][j-1] + sums[i-1][j]-sums[i-1][j-1])

# for i in matrix:
#     print(i)

# for j in sums:
#     print(j)

for _ in range(M):
    row_start, col_start, row_end, col_end = map(int, sys.stdin.readline().split())
    row_start -= 1
    col_start -= 1
    row_end -= 1
    col_end -= 1

    to_add = sums[row_end][col_end]
    to_sub = 0
    if row_start > 0:
        to_sub += sums[row_start-1][col_end]
    if col_start > 0:
        to_sub += sums[row_end][col_start-1]
    if row_start > 0 and col_start > 0:
        to_add += sums[row_start-1][col_start-1]

    print(to_add - to_sub)
