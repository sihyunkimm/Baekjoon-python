import sys

input = sys.stdin.readline

sites = {}

N, M = map(int, input().split())

for _ in range(N):
    domain, pw = input().split(' ')
    pw = pw.rstrip()
    sites[domain] = pw

for _ in range(M):
    search = input().rstrip()
    print(sites[search])

