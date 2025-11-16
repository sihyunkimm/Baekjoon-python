X = 0
Y = 1
VALUE = 2

n_list = []
for i in range(9):
  n_list.append(list(map(int, input().split())))

max_num = [0, 0, 0]
for i in range(9):
  for j in range(9):
    if n_list[i][j] > max_num[VALUE]:
      max_num[X] = i
      max_num[Y] = j
      max_num[VALUE] = n_list[i][j]

print(max_num[VALUE])
print(max_num[X] + 1, max_num[Y] + 1)
