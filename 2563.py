RAW = 100
COL = 100

c_paper_num = int(input())
paper = [[0 for j in range(COL)] for i in range(RAW)]
count = 0


def printPaper():
  for i in range(RAW):
    for j in range(COL):
      print(paper[i][j], end='')
    print()


for i in range(c_paper_num):
  x, y = map(int, input().split())
  for j in range(x, x + 10):
    for k in range(y, y + 10):
      paper[j][k] = 1

#printPaper()

for i in range(RAW):
  for j in range(COL):
    if paper[i][j] == 1:
      count += 1

print(count)
