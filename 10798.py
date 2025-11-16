word_list = []
for i in range(5):
  word_list.append(input())

max_len = -1
for i in range(5):
  if len(word_list[i]) > max_len:
    max_len = len(word_list[i])

for i in range(max_len):
  for j in range(5):
    if i < len(word_list[j]):
      print(word_list[j][i], end='')
