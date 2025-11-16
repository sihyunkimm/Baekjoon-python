N = int(input())

prime_list = []

def isPrime(n):
    i = 0
    while i < len(prime_list) and prime_list[i] <= n**(1/2):
        if n % prime_list[i] == 0:
            return False
        i += 1
    return True


for i in range(2, N+1):
    if isPrime(i):
        prime_list.append(i)

dp = [2]
for i in range(1, len(prime_list)):
    dp.append(dp[i-1] + prime_list[i])

left = -1
right = 0
case = 0
while right < len(dp):
    if left == -1:
        diff = dp[right]
    else:
        diff = dp[right] - dp[left]
    
    if diff < N:
        right += 1
    elif diff > N:
        left += 1
    else:
        case += 1
        right += 1

print(case)