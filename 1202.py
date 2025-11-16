import sys
from heapq import *

input = sys.stdin.readline
WEIGHT = 0
VALUE = 1

N, K = map(int, input().split())

gems = []
for _ in range(N):
    w, v = map(int, input().split())
    heappush(gems, (w, v))

bags = [int(input()) for _ in range(K)]
bags.sort()

stored_minus_gem_values = []
answer = 0
for bag in bags:
    while gems and bag >= gems[0][WEIGHT]:
        heappush(stored_minus_gem_values, -gems[0][VALUE])
        heappop(gems)
    answer += -heappop(stored_minus_gem_values) if stored_minus_gem_values else 0 

print(answer)