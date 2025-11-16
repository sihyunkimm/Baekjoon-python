n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

shirt_bundle = 0
for i in size:
  shirt_bundle += i // t
  if i % t != 0:
    shirt_bundle += 1

pen_bundle = sum(size) // p
pen_each = sum(size) % p

print(shirt_bundle)
print(pen_bundle, pen_each)