import sys

input = sys.stdin.readline

N = int(input())

numbers = [int(input()) for _ in range(N)]

numbers.sort()


def my_round(num):
    if num >= 0:
        if num - int(num) >= 0.5:
            return int(num) + 1
        else:
            return int(num)
    else:
        if num - int(num) >= -0.5:
            return int(num)
        else:
            return int(num) - 1


# 산술평균
print(int(my_round(sum(numbers) / len(numbers))))

# 중앙값
print(numbers[int(len(numbers) / 2)])

# 최빈값
num_dict = {}
for num in numbers:
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

max_numbers = []
max_count = 0
for key, value in num_dict.items():
    if value > max_count:
        max_numbers = [key]
        max_count = value
    elif value == max_count:
        max_numbers.append(key)
    else:
        pass

max_numbers.sort()

if len(max_numbers) == 1:
    print(max_numbers[0])
else:
    print(max_numbers[1])


# 최댓값 - 최솟값
print(numbers[-1] - numbers[0])