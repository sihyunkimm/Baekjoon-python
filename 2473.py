N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

result = (0, 0, 0)
min_abs = float('inf')

for i in range(N - 2):
    left = i + 1
    right = N - 1

    while left < right:
        current_sum = numbers[i] + numbers[left] + numbers[right]
        current_abs = abs(current_sum)

        if current_abs < min_abs:
            min_abs = current_abs
            result = (numbers[i], numbers[left], numbers[right])
        
        if current_sum > 0:
            right -= 1
        else:
            left += 1

print(*sorted(result))