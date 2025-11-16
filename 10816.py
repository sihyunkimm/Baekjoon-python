# 시간초과로 인해 해싱을 배웠음

num_card = int(input())
card_list = list(map(int, input().split()))
num_query = int(input())
query_list = list(map(int, input().split()))

hash = {}

for card in card_list:
  if card in hash:
    hash[card] += 1
  else:
    hash[card] = 1

for q in query_list:
  if q in hash:
    print(hash[q], end=' ')
  else:
    print(0, end=' ')
