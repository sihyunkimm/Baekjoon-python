import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
NULL = 0

N = int(input())

numbers = list(map(int, input().rstrip().split()))
dp = [[NULL for _ in range(N)] for _ in range(N)]

for i in range(N-1):
    dp[i][i] = True
    if numbers[i] == numbers[i+1]:
        dp[i][i+1] = True
    else:
        dp[i][i+1] = False
dp[-1][-1] = True

M = int(input())

def is_palindrome(s, e):
    if dp[s][e] != NULL:
        pass
    elif numbers[s] == numbers[e] and is_palindrome(s+1, e-1):
        dp[s][e] = True
    else:
        dp[s][e] = False

    return dp[s][e]
        
for _ in range(M):
    start, end = map(lambda x: x-1, map(int, input().rstrip().split()))
    if is_palindrome(start, end):
        print(1)
    else:
        print(0)