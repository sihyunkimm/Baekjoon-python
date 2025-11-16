import sys
import math

sys.setrecursionlimit(10**8)

A, B = map(int, input().split())

# 2**i - 1 까지 등장하는 1의 개수
dp = [0, 1]
i = 2

while 2**i < 10**16:
    dp.append(2*dp[i-1] + 2**(i-1))
    i += 1

def count(n):
    if n <= 0:
        return 0
    
    pow = int(math.log2(n))
    breakpoint = 2**pow

    if n == breakpoint:
        return dp[pow] + 1

    rest = n - breakpoint
    return dp[pow] + 1 + rest + count(rest)

print(count(B) - count(A-1))


def countManualTo(n):
    ans = 0
    for i in range(1, n+1):
        ans +=  str(bin(i))[2:].count('1')
    return ans


