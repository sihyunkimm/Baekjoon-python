import sys

input = sys.stdin.readline

N = int(input())

xys = []
for _ in range(N):
    xys.append(list(map(int, input().split())))
xys.append(xys[0])

answer = 0
for i in range(N):
    answer += xys[i][0] * xys[i+1][1] - xys[i+1][0] * xys[i][1]

print(abs(answer) / 2)
