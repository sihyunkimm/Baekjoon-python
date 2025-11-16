import sys

N, M = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))

sum_list = [num_list[0]]
for i in range(1, N):
    sum_list.append(sum_list[i-1] + num_list[i])

#print(sum_list)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    i -= 1
    j -= 1
    if i == 0:
        print(sum_list[j])
    else:
        print(sum_list[j] - sum_list[i-1])
