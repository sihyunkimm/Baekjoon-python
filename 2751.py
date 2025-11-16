import sys

N = int(sys.stdin.readline())

num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))

num.sort()

print('\n'.join(map(str, num)))
