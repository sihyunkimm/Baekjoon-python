import sys

numbers = []
N = int(sys.stdin.readline())

for _ in range(N):
    temp = int(sys.stdin.readline())
    if temp == 0:
        numbers.pop()
    else:
        numbers.append(temp)

print(sum(numbers))
