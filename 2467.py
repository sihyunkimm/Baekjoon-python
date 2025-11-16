N = int(input())

numbers = list(map(int, input().split()))

start = 0
end = N - 1

min_sum = float('inf')
answer = (numbers[start], numbers[end])

while start < end:
    cur_sum = numbers[start] + numbers[end]
    
    if abs(cur_sum) < abs(min_sum):
        min_sum = cur_sum
        answer = (numbers[start], numbers[end])

    if cur_sum > 0:
        end -= 1
    else:
        start += 1

print(answer[0], answer[1])