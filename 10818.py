min = 1000000
max = -1000000

n = int(input())
list_a = list(map(int, input().split()))


for i in list_a:

    if i < min:
        min = i
    
    if i > max:
        max = i

print(min, max)