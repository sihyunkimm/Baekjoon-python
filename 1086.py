import sys
from math import gcd, factorial

input = sys.stdin.readline

N = int(input())
num_str_list = [input().strip() for _ in range(N)]
K = int(input())

remainders = []
lengths = []
for s in num_str_list:
    remainders.append(int(s) % K)
    lengths.append(len(s))

ten_pow = [1] * 751
for i in range(1, 751):
    ten_pow[i] = (ten_pow[i-1] * 10) % K

# 숫자 집합 i(이진수)를 사용하여 나머지가 j가 되는 경우의 수 dp[i][j] 
dp = [[0] * K for _ in range(1 << N)]
dp[0][0] = 1

for used in range(1 << N):
    for rem in range(K):
        if dp[used][rem] == 0:
            continue
        
        for i in range(N):
            if not (used & (1 << i)):
                next_rem = (rem * ten_pow[lengths[i]] + remainders[i]) % K
                dp[used | (1 << i)][next_rem] += dp[used][rem]


p = dp[(1 << N) - 1][0]
q = factorial(N)

if p == 0:
    print("0/1")
else:
    common = gcd(p, q)
    print(f"{p // common}/{q // common}")