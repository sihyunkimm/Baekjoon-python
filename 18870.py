import sys


N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))


sorted_list = sorted(num_list)
num_dict = {}

value = 0
for i in sorted_list:
    if i not in num_dict:
        num_dict[i] = value
        value += 1


for n in num_list:
    print(num_dict[n], end=' ')
