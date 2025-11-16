N = int(input())
cords = []

for _ in range(N):
    cords.append(list(map(int, input().split())))

cords.sort()

for c in cords:
    print(*c)
