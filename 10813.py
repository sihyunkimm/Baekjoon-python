N, M = map(int, input().split())

bucket = []
for i in range(1, N + 1):
  bucket.append(i)

#print(bucket)

for i in range(M):
  a, b = map(int, input().split())
  bucket[a - 1], bucket[b - 1] = bucket[b - 1], bucket[a - 1]

for i in bucket:
  print(i, end=" ")

#print(bucket)
