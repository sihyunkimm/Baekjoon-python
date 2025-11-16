# 비트마스킹, sys.stdin.readline() 을 배웠음

import sys

cmd_num = int(input())

s = 0b0

for _ in range(cmd_num):
  str_input = sys.stdin.readline().rstrip().split()

  if str_input[0] == 'add':
    s |= 0b1 << int(str_input[1])
  elif str_input[0] == 'remove':
    s &= ~(0b1 << int(str_input[1]))
  elif str_input[0] == 'check':
    if s & 0b1 << int(str_input[1]):
      print(1)
    else:
      print(0)
  elif str_input[0] == 'toggle':
    s ^= 0b1 << int(str_input[1])
  elif str_input[0] == 'all':
    s = 0b111_111_111_111_111_111_111  # 이걸 뭔가 효율적으로 입력할 방법이 없을까
  elif str_input[0] == 'empty':
    s = 0b0
  else:
    print('fuckit')

  #print(format(s, 'b'))
