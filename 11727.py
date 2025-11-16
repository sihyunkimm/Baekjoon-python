n = int(input())

dp = [0, 1, 3]

i = 3
while i < n+1 :
    dp.append(dp[i-1] + dp[i-2]*2)
    i += 1

print(dp[n]%10007)