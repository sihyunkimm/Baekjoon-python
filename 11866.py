n, k = map(int, input().split())

num_list = list(range(1, n+1))

print('<', end='')

index_num = 0
while len(num_list) > 0:
  index_num = (index_num+k-1) % len(num_list)
  print(num_list.pop(index_num), end='')
  if len(num_list) > 0:
    print(', ', end='')

print('>')