import sys

N = int(sys.stdin.readline().rstrip())

meetings = []

for _ in range(N):
    meetings.append(tuple(map(int, sys.stdin.readline().split())))

meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
time = 0
for m in meetings:
    if time <= m[0]:
        time = m[1]
        count += 1

print(count)
