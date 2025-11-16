N, M = map(int, input().split())

bucket = []
for i in range(1, N + 1):
  bucket.append(i)

#print(bucket)

for i in range(M):
  start, end = map(int, input().split())
  #print(bucket[start - 1:end])
  bucket[start - 1:end] = bucket[start - 1:end][::-1]
  #print(bucket[start - 1:end])
  #print(bucket)

for i in bucket:
  print(i, end=" ")

#print(bucket)
