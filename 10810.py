N, M = map(int, input().split())

bucket = []
for i in range(N):
  bucket.append(0)

#print(bucket)

for i in range(M):
  start, end, ball = map(int, input().split())
  for j in range(start - 1, end):
    bucket[j] = ball

for i in bucket:
  print(i, end=" ")

#print(bucket)
