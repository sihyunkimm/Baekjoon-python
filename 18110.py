import sys

input = sys.stdin.readline


def my_round(value):
  if value - int(value) >= 0.5:
    return int(value) + 1
  else:
    return int(value)


n = int(input())

if n == 0:
  print(0)
  exit(0)


op = []
for _ in range(n):
    op.append(int(input()))

op.sort()

cut = my_round(n * 0.15)

if cut > 0:
    print( my_round(sum(op[cut:-cut]) / len(op[cut:-cut])) )
else:
    print( my_round(sum(op) / len(op)) )
