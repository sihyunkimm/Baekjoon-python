import sys
input = sys.stdin.readline
ID, X, Y = 1, 2
N = int(input())
cords = [[i, *map(int, input().split())] for i in range(N)] #[ID, X, Y]

cords.sort()
x_min, x_max = cords[0], cords[-1]

cords.sort(lambda x: x[Y])
y_min, y_max = cords[0], cords[-1]



start = y_max
visited = [False for _ in range(N)] # visited by id
visited[start[ID]] = True

def next_1(cord):
    min_slope = 0


# TODO 컨벡스 헐 알고리즘 알아보기