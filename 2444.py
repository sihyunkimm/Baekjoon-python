n = int(input())

for i in range(n):
  print(' ' * (n - i - 1) + '*' * (i * 2 + 1))

for i in range(n):
  print((' ' * (i + 1)) + '*' * ((n - i - 1) * 2 - 1))