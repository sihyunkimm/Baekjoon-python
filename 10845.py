cmd_num = int(input())


que = []

def push(n):
  que.append(n)

def pop():
  if len(que) == 0:
    return -1
  else:
    return que.pop(0)

def size():
  return len(que)

def empty():
  if len(que) == 0:
    return 1
  else:
    return 0

def front():
  if len(que) == 0:
    return -1
  else:
    return que[0]

def back():
  if len(que) == 0:
    return -1
  else:
    return que[len(que)-1]


for i in range(cmd_num):
  str_input = input()

  if 'push' in str_input:
    trash, n = str_input.split()
    push (int(n))
  elif 'pop' in str_input:
    print(pop())
  elif 'size' in str_input:
    print(size())
  elif 'empty' in str_input:
    print(empty())
  elif 'front' in str_input:
    print(front())
  elif 'back' in str_input:
    print(back())
  else:
    print('fuckit')

  #print(que)

