N = int(input())

cords = []

for _ in range(N):
    cords.append(list(map(int, input().split())))

cords.sort()
cords.sort(key=lambda x: x[1])

for c in cords:
    print(*c)
