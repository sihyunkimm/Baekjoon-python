import sys

input = sys.stdin.readline
A, B, C, D = 0, 1, 2, 3
MAXIMUM = 2**28 + 1

N = int(input())
arrs = [list() for _ in range(4)]


for _ in range(N):
    temp = list(map(int, input().split()))
    for i in range(4):
        arrs[i].append(temp[i])

AnB = []
for a in range(N):
    for b in range(N):
        AnB.append(arrs[A][a] + arrs[B][b])
AnB.sort()

CnD = []
for c in range(N):
    for d in range(N):
        CnD.append(arrs[C][c] + arrs[D][d])
CnD.sort()

left, right = 0, len(AnB) - 1
answer = 0
while left <= len(AnB) - 1 and right >= 0:
    abcd = AnB[left] + CnD[right]
    if abcd == 0:
        start = left
        x = 0
        while left <= len(AnB) - 1 and AnB[left] == AnB[start]:
            x += 1
            left += 1

        end = right
        y = 0
        while right >= 0 and CnD[right] == CnD[end]:
            y += 1
            right -= 1
        
        answer += x*y
        
    elif abcd < 0:
        left += 1
    else:
        right -= 1

print(answer)