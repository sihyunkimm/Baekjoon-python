num = int(input())
g_num = 0

for i in range(num):
  word = input()
  is_g = True
  a_list = []

  j = 0
  while j < len(word):

    if word[j] in a_list:
      is_g = False
      #print(word[j], a_list, j)
      break
    else:
      a_list.append(word[j])

    while j + 1 < len(word):
      if word[j] == word[j + 1]:
        j += 1
        #print(j)
      else:
        break

    j += 1

  #print(is_g)

  if is_g:
    g_num += 1

print(g_num)
