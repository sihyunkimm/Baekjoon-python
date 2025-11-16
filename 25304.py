total = int(input())
type = int(input())
total_price = 0
for i in range(type):
  price, num = map(int, input().split())
  total_price += price * num

if total == total_price:
  print("Yes")
else:
  print("No")
