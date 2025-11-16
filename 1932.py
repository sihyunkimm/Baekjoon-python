import sys

n = int(input())
num_list = []

for _ in range(n):
    num_list.append(list(map(int, sys.stdin.readline().split())))

sum_list= [[num_list[0][0]]]

for i in range(1, n):
    sum_list.append([])
    for j in range(i+1):
        if j == 0:
            sum_list[i].append(sum_list[i-1][0] + num_list[i][0])
        elif j == i:
            sum_list[i].append(sum_list[i-1][-1] + num_list[i][j])
        else:
            sum_list[i].append(num_list[i][j] + max(sum_list[i-1][j-1], sum_list[i-1][j]))

print(max(sum_list[-1]))
