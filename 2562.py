max = 0
num = 0
temp = 0

for i in range(9):
    temp = int(input())
    if temp > max:
        max = temp
        num = i + 1

print(max)
print(num)