n = int(input())

time_list = list(map(int, input().split()))

time_list.sort()

sum = 0
time = 0
for i in time_list:
    time += i
    sum += time

print(sum)
