import sys
input = sys.stdin.readline
NUM_RANGE = 10 # 0~9
BIT_RANGE = 1 << NUM_RANGE # 9876543210 (0b0 ~ 0b1111111111) -> total 1024 (1023까지)
MOD = 10**9

n = int(input())
dp = [[[0]*(BIT_RANGE) for _ in range(NUM_RANGE)] for _ in range(n+1)]

# 한자리 수 부터 시작하려면 한자리수들 다 1로 초기화
# 1 예시 0b0000000010
for k in range(NUM_RANGE):
  dp[1][k][1<<k] = 1

for i in range(1,n): # n-1까지하면 n 구할수 있음
  for j in range(NUM_RANGE):
    for b in range(BIT_RANGE):
      if 0<=j<9:
        more = b | 1<<(j+1)
        dp[i+1][j+1][more] += dp[i][j][b]
        dp[i+1][j+1][more] %= MOD
      if 0<j<=9:
        less = b | 1<<(j-1)
        dp[i+1][j-1][less] += dp[i][j][b]
        dp[i+1][j-1][less] %= MOD

total = 0
for k in range(1,NUM_RANGE): # 0으로 시작하는 수만 제외
  total += dp[n][k][0b1111111111]
  total%=MOD
print(total)