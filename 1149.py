import sys

N = int(sys.stdin.readline())
rgb = []
for _ in range(N):
    rgb.append(list(map(int, sys.stdin.readline().split())))

sum = [[0 for _ in range(3)]for _ in range(N)]

sum[0] = rgb[0]

for i in range(1, N):
    sum[i][0] = rgb[i][0] + min(sum[i-1][1], sum[i-1][2])
    sum[i][1] = rgb[i][1] + min(sum[i-1][0], sum[i-1][2])
    sum[i][2] = rgb[i][2] + min(sum[i-1][0], sum[i-1][1])

print(min(sum[-1]))
