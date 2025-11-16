N = int(input())

dudes = []
for _ in range(N):
    dudes.append(tuple(map(int, input().split())))

ranks = []
for i in range(N):
    count = 1
    for j in range(N):
        if dudes[i][0] < dudes[j][0] and dudes[i][1] < dudes[j][1]:
            count += 1
    ranks.append(count)

print(*ranks)
