import sys

input = sys.stdin.readline

n, m = map(int, input().split())

poke_by_name = {}
poke_by_num = {}
for i in range(1, n+1):
    temp = input().rstrip()
    poke_by_name[temp] = i
    poke_by_num[i] = temp



for _ in range(m):
    str_in = input().rstrip()
    if str_in.isalpha():
        print(poke_by_name[str_in])
    else:
        print(poke_by_num[int(str_in)])