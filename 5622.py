word = input()
t = 0
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

for i in word:
  for j in dial:
    if i in j:
      t += dial.index(j) + 3

print(t)
