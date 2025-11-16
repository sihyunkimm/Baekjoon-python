import sys

N, K = map(int, sys.stdin.readline().split())
wNv_list = []

for _ in range(N):
    wNv_list.append(list(map(int, sys.stdin.readline().split())))
    
table = [[0 for _ in range(K+1)] for _ in range(N)]

for i in range(N):
    for weight in range(K+1):
        if weight >= wNv_list[i][0]:
            if i == 0:
                table[i][weight] = wNv_list[i][1]
            else:
                table[i][weight] = max(wNv_list[i][1] + table[i-1][weight - wNv_list[i][0]], table[i-1][weight])
        else:
            table[i][weight] = table[i-1][weight]

print(table[-1][-1])
