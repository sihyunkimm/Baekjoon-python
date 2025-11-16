N, S = map(int, input().split())
numbers = list(map(int, input().split()))

min_len = N + 1
start, end = 0, 0
num_sum = numbers[end]

while start <= end < N:
    if num_sum >= S:
        if min_len > end - start + 1:
            min_len = end - start + 1
        num_sum -= numbers[start]
        start += 1
    else:
        end += 1
        if end >= N:
            break
        num_sum += numbers[end]

if min_len > N:
    print(0)
else:
    print(min_len)