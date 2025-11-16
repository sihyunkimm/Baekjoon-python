max = 0
n = int(input())
original_list = list(map(int, input().split()))
manipulated_list = []
total = 0
average = 0

# print(original_list)

for i in original_list:
    if i > max:
        max = i

# print(max)

for i in original_list:
    manNum = i/max*100
    manipulated_list.append(manNum)

# print(manipulated_list)

for i in manipulated_list:
    total = total + i

# print(total)

average = total / len(manipulated_list)

print(average)