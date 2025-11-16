import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    stickers = []
    sums = [[],[]]
    
    for _ in range(2):
        stickers.append(list(map(int, sys.stdin.readline().split())))

    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
        continue

    sums[0].append(stickers[0][0])
    sums[1].append(stickers[1][0])
    sums[0].append(sums[1][0] + stickers[0][1])
    sums[1].append(sums[0][0] + stickers[1][1])
    
    for i in range(2, n):
        sums[0].append(stickers[0][i] + max(sums[0][i-2], sums[1][i-2], sums[1][i-1]))
        sums[1].append(stickers[1][i] + max(sums[0][i-2], sums[1][i-2], sums[0][i-1]))

    print(max(map(max, sums)))
