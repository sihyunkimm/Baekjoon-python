N = int(input())
numlist = set(map(int, input().split()))
M = int(input())
q = list(map(int, input().split()))

for num in q:
    if num in numlist:
        print(1)
    else:
        print(0)
